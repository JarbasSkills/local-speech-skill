from mycroft import MycroftSkill, intent_file_handler


class LocalSpeech(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('speech.local.intent')
    def handle_speech_local(self, message):
        self.speak_dialog('speech.local')


def create_skill():
    return LocalSpeech()

