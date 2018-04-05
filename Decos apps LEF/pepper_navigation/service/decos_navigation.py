#!/usr/bin/env python
import qi
import sys
import os
import numpy
from PIL import Image
import base64
import cStringIO
from exploration import Exploration

class DecosNavigation:
    services_connected = None

    def __init__(self, application):
        # Getting a session that will be reused everywhere
        self.application = application
        self.session = application.session
        self.service_name = self.__class__.__name__

        # Getting a logger. Logs will be in /var/log/naoqi/servicemanager/{application id}.{service name}
        self.logger = qi.Logger(self.service_name)

        # Do some initializations before the service is registered to NAOqi
        self.logger.info("Initializing...")
        self.connect_services()

        self.logger.info("Initialized!")


    @qi.nobind
    def start_service(self):
        self.logger.info("Starting service...")
        self.logger.info("Started!")

    @qi.nobind
    def stop_service(self):
        # probably useless, unless one method needs to stop the service from inside.
        # external naoqi scripts should use ALServiceManager.stopService if they need to stop it.
        self.logger.info("Stopping service...")
        self.application.stop()
        self.logger.info("Stopped!")

    @qi.nobind
    def connect_services(self):
        # connect all services required by your module
        # done in async way over 30s,
        # so it works even if other services are not yet ready when you start your module
        # this is required when the service is autorun as it may start before other modules...
        self.logger.info('Connecting services...')
        self.services_connected = qi.Promise()
        services_connected_fut = self.services_connected.future()

        def get_services():
            try:
                self.memory = self.session.service('ALMemory')

                self.motion_service=self.session.service("ALMotion")
                self.decos_navigation_files_service=self.session.service("DecosNavigationFiles")
                self.navigation_service=self.session.service("ALNavigation")

                self.exploration = Exploration(self.navigation_service,self.motion_service,self.decos_navigation_files_service)

                self.logger.info('All services are now connected')
                self.services_connected.setValue(True)
            except RuntimeError as e:
                self.logger.warning('Still missing some service:\n {}'.format(e))

        get_services_task = qi.PeriodicTask()
        get_services_task.setCallback(get_services)
        get_services_task.setUsPeriod(int(2*1000000))  # check every 2s
        get_services_task.start(True)
        try:
            services_connected_fut.value(30*1000)  # timeout = 30s
            get_services_task.stop()
        except RuntimeError:
            get_services_task.stop()
            self.logger.error('Failed to reach all services after 30 seconds')
            raise RuntimeError


    ### Utility functions ###
    def load(self):
        # how to load and display the webpage on the tablet
        folder = self.app_uuid
        self.logger.info("Loading tablet page for app: {}".format(folder))
        try:
            self.ts.loadApplication(folder)
        except Exception, e:
            self.logger.info("Error while loading tablet: {}".format(e))

    def show_local(self,page):
        self.show('http://198.18.0.1/apps/'+self.app_uuid+'/'+page)

    def show(self,page):
        print("Showing a new page")
        self.ts.showWebview(page)

    def createMap(self, radius):
        return self.exploration.createMap(radius)

    def loadMap(self,name):
        return self.exploration.loadMap(name)


    def getMap(self, name):
        return self.exploration.getMap(name)
        """
        navigation_files = self.decos_navigation_files_service
        return navigation_files.getMap(name)
        """

    def getMetricalMap(self):
        return self.exploration.getMetricalMap()
        #return self.navigation_service.getMetricalMap()

    def getMapName(self):
        return self.exploration.getMapName()

    def getJpegMap(self):
        result_map = self.navigation_service.getMetricalMap()

        origin = [ result_map[3][0]/result_map[0] , result_map[3][1]/result_map[0] ]
        print "Origin is at " + str(origin)

        map_width = result_map[1]
        map_height = result_map[2]
        img = numpy.array(result_map[4]).reshape(map_width, map_height).T
        img = (100 - img) * 2.55 # from 0..100 to 255..0
        img = numpy.array(img, numpy.uint8)
        img = Image.fromarray(img)

        buffer = cStringIO.StringIO()
        img.save(buffer, format="JPEG")

        return base64.b64encode(buffer.getvalue())

    def uploadMap(self,data,name):
        navigation_files = self.decos_navigation_files_service
        navigation_files.uploadMap(data,name)

    def start(self):
        qi.async(self.navigation_service.startLocalization)

    def localize(self):
        self.navigation_service.relocalizeInMap([0,0,0])

    def stop(self):
        qi.async(self.motion_service.stopMove)
        qi.async(self.navigation_service.stopLocalization)
        return qi.async(self.navigation_service.stopExploration)

    def goTo(self,x,y):
        return qi.async(self.exploration.goTo,x,y)

    def goToPixel(self,x,y):
        return qi.async(self.exploration.goToPixel,x,y)

    def getGoal(self):
        return qi.async(self.exploration.getGoal)

    def getPosition(self):
        return qi.async(self.exploration.getPosition)

    def getPositionInPixels(self):
        return qi.async( self.exploration.getPositionInPixels)

    def getHomePosition(self):
        return qi.async(self.exploration.getHomePosition)


    def showMapOnTablet(self):
        try:
            tabletService = self.session.service("ALTabletService")

            # Display a web page on the tablet
            tabletService.showWebview("http://192.168.8.104/apps/decos-navigation-service/show_map.html")

        except Exception, e:
            print "Error was: ", e


    ### ################# ###

    def cleanup(self):
        # called when your module is stopped
        self.logger.info("Cleaning...")
        # do something
        self.logger.info("End!")

if __name__ == "__main__":
    # with this you can run the script for tests on remote robots
    # run : python my_super_service.py --qi-url 123.123.123.123
    app = qi.Application(sys.argv)
    app.start()
    service_instance = DecosNavigation(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    service_instance.start_service()
    app.run()
    service_instance.cleanup()
    app.session.unregisterService(service_id)
