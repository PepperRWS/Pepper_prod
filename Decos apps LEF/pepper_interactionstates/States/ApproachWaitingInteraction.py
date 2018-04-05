import json
import qi

class ApproachWaitingInteraction:
    def __init__(self,session):
        self.session= session
        self.service_name = self.__class__.__name__
        self.logger = qi.Logger(self.service_name)
        self.awareness = self.session.service('ALBasicAwareness')
        self.memory = self.session.service("ALMemory")
        self.engagement = self.session.service("ALEngagementZones")
        self.people_perception = self.session.service("ALPeoplePerception")
        self.motion = self.session.service("ALMotion")
        self.subscribeDone = False
        filepath = "./config/ApproachWaitingInteraction.json"
        configfile= open(filepath).read()
        self.tracker = self.session.service( "ALTracker" )
        self.config= json.loads(configfile)
        self.take_initiative = self.config["take_initiative"]
        self.move_distance = self.config["move_distance"] / 100.0

        pass

    def start(self):
        self.logger.info("Start ApproachWaitingInteraction")
        self.awareness.setEngagementMode('FullyEngaged')
        self.awareness.setTrackingMode('Head')
        self.awareness.setStimulusDetectionEnabled('Sound', True)
        self.awareness.setStimulusDetectionEnabled('Movement', True)
        self.awareness.setStimulusDetectionEnabled('People', True)
        self.awareness.setStimulusDetectionEnabled('Touch', True)
        # if tracker was still active, unregister previous targets
        self.tracker.unregisterAllTargets()

        try:
            moved = self.memory.getData("Decos/movedToFront")
            self.motion.moveTo(-moved, 0.0, 0.0 )
        except:
            self.logger.info("Value not set")

        self.startAngle = 0.0
        self.peopleSeen = 0
        if (not self.subscribeDone):
            self.subscriberArrived = self.memory.subscriber("PeoplePerception/JustArrived")
            self.subscriberArrived.signal.connect(self.on_people_arrived)
            self.subscriberLeft = self.memory.subscriber("PeoplePerception/JustLeft")
            self.subscriberLeft.signal.connect(self.on_people_left)
            self.subscribeDone = True

        self.saveValues = []
        self.saveValues.append(self.engagement.getLimitAngle())
        self.saveValues.append(self.people_perception.getTimeBeforePersonDisappears())
        self.saveValues.append(self.people_perception.getMaximumDetectionRange())
        self.saveValues.append(self.motion.getOrthogonalSecurityDistance())
        self.saveValues.append(self.motion.getTangentialSecurityDistance())

        self.engagement.setLimitAngle(25.0)
        #self.engagement.setFirstLimitDistance(1.0)
        self.people_perception.setTimeBeforePersonDisappears(1.0)
        self.people_perception.setMaximumDetectionRange(2.0)
        self.people_perception.resetPopulation()
        self.distance = self.move_distance
        self.motion.setOrthogonalSecurityDistance(0.1)
        self.motion.setTangentialSecurityDistance(0.1)
        
        self.awareness.startAwareness()

    def greetPerson(self):
        if (self.peopleSeen > 0):
            # is person still there, then continue else quit
            self.startAngle = 0.0
            result = self.motion.moveTo(self.distance, 0.0, self.startAngle)
            if (result):
                self.memory.insertData("Decos/movedToFront", self.distance)
            else:
                self.logger.info("move front result " + str(result))

    def on_people_arrived(self, id):
        self.logger.info("on_people_arrived " + str(id))
        if (self.peopleSeen == 0):
            self.peopleSeen = id
            #self.awareness.pauseAwareness()
            #self.tracker.registerTarget("People", id)
            #lookAt([1.1,0,1], 0, 0.5, False)
            # is person still there, then continue else quit
            self.waiting = qi.async(self.greetPerson, delay=int(1 * 1000 * 1000))

    def on_people_left(self, id):
        self.logger.info("on_people_left " + str(id))
        if (self.peopleSeen == id):
            moved = self.memory.getData("Decos/movedToFront")
            result = self.motion.moveTo(-moved, 0.0, -self.startAngle)
            if (result):
               self.memory.insertData("Decos/movedToFront", 0)
            else:
                self.logger.info("move back result " + str(result))
            #self.awareness.resumeAwareness()
            self.peopleSeen = 0

    def stop(self):
        self.logger.info("Stop ApproachWaitingInteraction")
        self.awareness.stopAwareness()
        # unregister the subscribers
        self.subscriberArrived = None
        self.subscriberLeft = None
        self.tracker.unregisterAllTargets()
        self.peopleSeen = False
        # Reset values back to when started
        self.engagement.setLimitAngle(self.saveValues[0])
        self.people_perception.setTimeBeforePersonDisappears(self.saveValues[1])
        self.people_perception.setMaximumDetectionRange(self.saveValues[2])
        self.motion.setOrthogonalSecurityDistance(self.saveValues[3])
        self.motion.setTangentialSecurityDistance(self.saveValues[4])
        # do not go back here, since the interaction starts
        #moved = self.memory.getData("Decos/movedToFront")
        #result = self.motion.moveTo(-moved, 0.0, -self.startAngle)
        #if (result):
        #   self.memory.insertData("Decos/movedToFront", 0)
