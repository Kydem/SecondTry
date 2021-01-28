import os
import codecs
import json

class SecondtrySettings(object):
    def __init__(self, settingsfile=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:
            self.ScumMessage = "Prepare to be eaten, bourgeoisie SCUM!"
            self.PoorBoyMessage = "I hope you brought a fork, Gutter Rat!"
            self.Odds = 10
            self.Command = "!EatTheRich"

    def Reload(self, jsondata):
        self.__dict__ = json.loads(jsondata, encoding="utf-8")
        return

    def Save(self, settingsfile):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8")
            with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
        except:
            Parent.Log(ScriptName, "Failed to save settings to file.")
        return