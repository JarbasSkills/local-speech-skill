from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import create_daemon
from mycroft.util.signal import create_signal
from mycroft.messagebus.message import Message
from kaldi_spotter import KaldiWWSpotter
import json

class LocalSpeech(MycroftSkill):
    def initialize(self):
        self.settings.set_changed_callback(self.handle_settings_changed)
        if "hotwords" not in self.settings:
            self.settings["hotwords"] = {}
            
        self.kaldi = KaldiWWSpotter()
        self.kaldi.on("hotword", self.handle_hotword)
        
        for hw in self.settings["hotwords"]:
            self.kaldi.add_hotword(hw, self.settings["hotwords"][hw])
        create_daemon(self.kaldi.run)

    def handle_settings_changed(self):
        # dynamic update of words
        if self.settings.get("new_word"):
            name = self.settings["new_word"]
            s = self.settings.get("new_sensitivity", 0.2)
            self.settings["hotwords"][name] = {"transcriptions": [name], "intent": "listen", "sensitivity": s}
        
        if self.settings.get("delete_word"):
            name = self.settings["delete_word"]
            if name in self.settings["hotwords"]:
                self.settings["hotwords"].pop(name)
        
        # remove words if deleted
        for hw in self.kaldi.hotwords:
            if hw not in self.settings["hotwords"]:
                self.kaldi.remove_hotword(hw)
                
        # add new words
        for hw in self.settings["hotwords"]:
            if hw not in self.kaldi.hotwords:
                self.kaldi.add_hotword(hw, self.settings["hotwords"][hw])
    
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

