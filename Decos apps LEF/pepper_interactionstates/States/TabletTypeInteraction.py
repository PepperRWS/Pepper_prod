

class TabletTypeInteraction:
    def __init__(self,session):
        self.session= session
        self.awareness = self.session.service('ALBasicAwareness')
        self.tracker = self.session.service( "ALTracker" )

        self.moveListen = self.session.service("ALListeningMovement")
        self.moveSpeak = self.session.service("ALSpeakingMovement")

        self.behavior_manager = self.session.service("ALBehaviorManager")

    def start(self):
        print("Start TabletTypeInteraction")

        #self.awareness.setEngagementMode('FullyEngaged')
        #self.awareness.setTrackingMode('Head')
        self.awareness.setStimulusDetectionEnabled('Sound', False)
        self.awareness.setStimulusDetectionEnabled('Movement', False)
        self.awareness.setStimulusDetectionEnabled('People', False)
        self.awareness.setStimulusDetectionEnabled('Touch', False)
        self.awareness.stopAwareness()

        self.moveListen.setEnabled(False)
        self.moveSpeak.setEnabled(False)

        #self.behavior_manager.runBehavior('animations/Stand/Gestures/ShowTablet_1')
        self.tracker.lookAt([1.1,0,1], 0, 0.5, False)

    def stop(self):
        self.awareness.stopAwareness()
        self.moveListen.setEnabled(True)
        self.moveSpeak.setEnabled(True)
