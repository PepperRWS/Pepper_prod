#! /usr/bin/env python

import qi

class Exploration:
    """
    Decos Exploration

    Contains a wrapper around the naoqi version 2.5.5 Exploration
    and localization library.
    """

    def __init__(self, navigation_service, motion_service , navigation_files):
        """
        Initializes the underlying naoqi services.
        """
        self.navigation_service = navigation_service
        self.motion_service = motion_service
        self.navigation_files = navigation_files

        self.current_goal = [0,0] # value in pixels
        self.home_position = [0,0] # value in pixels
        self.map_name = "Not loaded"

    def createMap(self, radius):
        """
        Creates the map using the exploration API from naoqi.

        Args:
            radius: Exploration radius in meters.
        Returns:
            image: Raw map image, grey, 0 for obstacle 255 for free space;
                   None if exploration failed.
        """

        if not self.motion_service.robotIsWakeUp():
            self.motion_service.wakeUp()

        error_code = self.navigation_service.explore(radius)
        if error_code != 0:
            return None

        path = self.navigation_service.saveExploration()
        print "Exploration saved at path: \"" + path + "\""
        return path

    def loadMap(self,name):
        self.map_name=name
        map =  self.navigation_service.loadExploration("/home/nao/.local/share/Explorer/"+name)

        metrical_map = self.getMetricalMap()
        self.mpp = metrical_map[0]
        self.offset = [ metrical_map[3][0] , metrical_map[3][1] ]

        return map

    def getMap(self,name):
        return self.navigation_files.getMap(name)

    def getMetricalMap(self):
        return self.navigation_service.getMetricalMap()

    def getMapName(self):
        return self.map_name

    def uploadMap(self,data,name):
        self.map_name = name
        self.navigation_files.uploadMap(data,name)

    def goTo(self,x,y):
        self.current_goal[0]= (x-self.offset[0])/self.mpp
        self.current_goal[1]= -1*(y-self.offset[1])/self.mpp

        return self.navigation_service.navigateToInMap([x,y,0])

    def goToPixel(self, x , y):
        goal_x = x * self.mpp + self.offset[0]
        goal_y = - y * self.mpp + self.offset[1]
        self.current_goal=[x,y]

        print "New pixel goal is to "+str([ goal_x , goal_y ])

        return self.navigation_service.navigateToInMap([ goal_x , goal_y ,0])

    def getGoal(self):
        return self.current_goal

    def getPosition(self):
        return self.navigation_service.getRobotPositionInMap()

    def getPositionInPixels(self):
        position_in_meters = self.getPosition()[0]
        x = int((position_in_meters[0]-self.offset[0])/self.mpp)
        y = int(-1*(position_in_meters[1]-self.offset[1])/self.mpp)

        return [x,y]

    def getHomePosition(self):
        self.home_position[0]= (0-self.offset[0])/self.mpp
        self.home_position[1]= -1*(0-self.offset[1])/self.mpp
        return self.home_position
