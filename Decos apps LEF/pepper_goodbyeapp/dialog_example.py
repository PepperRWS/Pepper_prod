import os

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.dialog = ALProxy('ALDialog')

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        # Deactivate topic
        self.dialog.deactivateTopic(self.topic)

        # Unload topic
        self.dialog.unloadTopic(self.topic)

        # Stop dialog
        self.dialog.unsubscribe(self.getName())

    def onInput_onStart(self):
        self.client_language = "enu"

        self.directory = tempfile.mkdtemp()
        try:
            os.stat(self.directory)
        except:
            os.mkdir(self.directory)

        self.topicname = "First_HR_Int_"+self.client_language+".top"
        topicPath = os.path.join(self.directory, self.topicname)

        dialog = self.generateTopicContent()
        with open(topicPath, 'w') as topic:
            topic.write(dialog)

        self.topic = self.dialog.loadTopic(topicPath.encode('utf-8'))

        # Start dialog
        self.dialog.subscribe(self.getName())

        self.dialog.activateTopic(self.topic)


    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box

    def generateTopicContent(self):
        dialog = """topic: ~First_HR_Int() \nlanguage: """+self.client_language+"""\nu:([hello hey])Hello there!!\n"""
        return dialog
