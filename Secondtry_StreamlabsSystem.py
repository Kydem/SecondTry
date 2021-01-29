#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from SecondtrySettings_Module import MySettings
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Bourgeoisie Detector"
Website = "https://www.twitch.tv/germansausagesarezewurst"
Description = "Find those rich scum!"
Creator = "GermanSausages"
Version = "1.0.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
SecondtrySettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
SecondtrySettings = MySettings()

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    Log("Init Called")
    EnsureLocalDirectoryExists("settings")

    SecondtrySettings = MySettings(SecondtrySettingsFile)
    Log("Init Ended")
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    Log("Execute Called")
    if not data.IsChatMessage() or not data.IsFromTwitch():
        return
    Log("Execute Is Chat Message")

    if SecondtrySettings.Command.lower() in data.Message.lower():
        number = Parent.GetPoints("germansausagesarezewurst")
        if number < SecondtrySettings.Currency:
            SendMessage(SecondtrySettings.ScumMessage)
        else:
            SendMessage(SecondtrySettings.PoorBoyMessage)
    
    Log("Execute Ended")
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    return parseString

#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SecondtrySettingsFile)
    return

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return

def EnsureLocalDirectoryExists(dirName):
    directory = os.path.join(os.path.dirname(__file__), dirName)
    if not os.path.exists(directory):
        os.makedirs(direcotory) 

def Log(message):
    Parent.Log("Secondtry", str(message))
    return

def SendMessage(message):
    Parent.SendStreamMessage(message)
    return