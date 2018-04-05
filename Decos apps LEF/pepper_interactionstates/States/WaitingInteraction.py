

class WaitingInteraction:
    def __init__(self,session):
        self.session= session
        self.tts = self.session.service("ALTextToSpeech")
        self.awareness = self.session.service('ALBasicAwareness')
        self.people_perception = self.session.service('ALPeoplePerception')

    def start(self):
        print("Waiting Interaction")

        self.awareness.setEngagementMode('FullyEngaged')
        self.awareness.setTrackingMode('BodyRotation')
        self.awareness.setStimulusDetectionEnabled('Sound', True)
        self.awareness.setStimulusDetectionEnabled('Movement', True)
        self.awareness.setStimulusDetectionEnabled('People', True)
        self.awareness.setStimulusDetectionEnabled('Touch', True)

        self.people_perception.setFastModeEnabled(True)
        self.awareness.startAwareness()

    def stop(self):
        self.people_perception.setFastModeEnabled(False)
        self.awareness.stopAwareness()
