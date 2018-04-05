import threading, time

class HumanTrackerThread(threading.Thread):
    def __init__(self, state):
        threading.Thread.__init__(self)
        self.state = state
        self.is_running = True

    def run(self):
        while self.is_running:
            time.sleep(1)
            current_user = self.state.get_current_user()

            print current_user
            print self.state.is_current_in_zone1()

            if not self.state.is_current_in_zone1() and current_user > -1:
                self.state.set_current_user(current_user)
                print "Changing focus to new user!"

    def stop(self):
        self.is_running = False

class DefaultInteraction:
    def __init__(self,session):
        self.session= session
        self.tts = self.session.service("ALTextToSpeech")
        self.awareness = self.session.service('ALBasicAwareness')
        self.engagement_zones = self.session.service('ALEngagementZones')
        self.people_perception = self.session.service('ALPeoplePerception')
        self.tracker = self.session.service( "ALTracker" )
        self.memory = self.session.service( "ALMemory" )

    def start(self):
        print("Default Interaction")

        self.awareness.setEngagementMode('FullyEngaged')
        self.awareness.setTrackingMode('Head')
        #self.awareness.setStimulusDetectionEnabled('Sound', True)
        #self.awareness.setStimulusDetectionEnabled('Movement', True)
        #self.awareness.setStimulusDetectionEnabled('People', True)
        #self.awareness.setStimulusDetectionEnabled('Touch', True)
        #self.awareness.startAwareness()
        self.awareness.setStimulusDetectionEnabled('Sound', False)
        self.awareness.setStimulusDetectionEnabled('Movement', False)
        self.awareness.setStimulusDetectionEnabled('People', False)
        self.awareness.setStimulusDetectionEnabled('Touch', False)
        self.awareness.stopAwareness()
        self.tracker.lookAt([1.1,0,1], 0, 0.5, False)

        # Maybe for the future
        #self.people_perception.setFastModeEnabled(True)
        #self.tracker_thread = HumanTrackerThread(self)
        #self.tracker_thread.start()
        #self.engagement_zones.setLimitAngle(30)

        # GET ALBasicAwareness/HumanTracked to get the current human being tracked
        # GET Event: "PeoplePerception/VisiblePeopleList" get current visible people list
        # check if the current human being tracked is in engagement zone one
        # if not:
        # check if there is a human in engagement zone one
        # if yes:
        # bool ALBasicAwarenessProxy::engagePerson(const int idPersonToEngage)   to forge engagement to the person in engagement zone one.


        # ON Event: "EngagementZones/PersonEnteredZone1"
        # check if the current human being tracked is in engagement zone one
        # if not:
        # check if there is a human in engagement zone one
        # if yes:
        # bool ALBasicAwarenessProxy::engagePerson(const int idPersonToEngage)   to forge engagement to the person in engagement zone one.

    def stop(self):
        #self.people_perception.setFastModeEnabled(False)
        #self.tracker_thread.stop()
        self.awareness.stopAwareness()
        self.engagement_zones.setLimitAngle(180)


    ## Custom Methods ##
    def get_current_user(self):
        return self.memory.getData("ALBasicAwareness/HumanTracked")

    def set_current_user(self,user):
        return self.awareness.engagePerson(user)

    def get_visible_users(self):
        #People that pepper can see with its face
        return self.memory.getData("PeoplePerception/VisiblePeopleList")

    def get_people_detected(self):
        return self.memory.getData("PeoplePerception/PeopleDetected")

    def get_people_in_zone1(self):
        return self.memory.getData("EngagementZones/PeopleInZone1")

    def is_current_in_zone1(self):
        current_user = self.get_current_user()
        people_in_zone1 = self.get_people_in_zone1()
        return current_user in people_in_zone1
