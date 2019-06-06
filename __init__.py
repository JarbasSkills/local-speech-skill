from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import create_daemon
from mycroft.util.signal import create_signal
from mycroft.messagebus.message import Message
from kaldi_spotter import KaldiWWSpotter
import json

class LocalSpeech(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    
    def initialize(self):
        self.kaldi = KaldiWWSpotter()
        self.kaldi.on("hotword", self.handle_hotword)
        create_daemon(self.kaldi.run)

    def handle_hotword(self, event):
        event = json.loads(event)
        data = event["data"]
        if data["intent"] == "listen":
            self.bus.emit(Message('recognizer_loop:wakeword', data))
            create_signal('startListening')
        else:
            data["utterances"] = [data["utterance"]]
            data.pop["utterance"]
            self.bus.emit(Message('recognizer_loop:utterance', data))
        
def create_skill():
    return LocalSpeech()

