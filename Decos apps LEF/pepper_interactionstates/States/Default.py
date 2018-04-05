

class Default:
    def __init__(self,session):
        self.session= session
        self.tts = self.session.service("ALTextToSpeech")
        self.awareness = self.session.service('ALBasicAwareness')

    def start(self):
        self.tts.say("Test!!")

        self.awareness.setEngagementMode('FullyEngaged')
        self.awareness.setTrackingMode('BodyRotation')
        self.awareness.setStimulusDetectionEnabled('Sound', True)
        self.awareness.setStimulusDetectionEnabled('Movement', True)
        self.awareness.setStimulusDetectionEnabled('People', True)
        self.awareness.setStimulusDetectionEnabled('Touch', True)


        self.awareness.startAwareness()

    def stop(self):
        self.awareness.stopAwareness()
