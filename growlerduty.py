#!/usr/bin/env python2 
import gntp.notifier
from pygermeister import PygerMeister

class Growlerduty(PygerMeister):
    def __init__(self, confFile="~/.pygerrc"):
        PygerMeister.__init__(self,confFile)
        self.defaults["growlHost"] = "127.0.0.1"
        self.defaults["growlPass"] = "" 
        self.defaults["growlPort"] = "23053"
        self.config = self.getConfig(confFile)

    def run(self):
        self.growl = gntp.notifier.GrowlNotifier(applicationName="Growlerduty",notifications=["Incident"],hostname=self.config.get("settings","growlHost"),password=self.config.get("settings","growlPass"),port=self.config.get("settings","growlPort"))
        self.growl.register()
        PygerMeister.run(self)

    def sendIncident(self,subject,message):
        if self.args.verbose:
            print "Sending incident popup (%s - %s)" % (subject,message)

        self.growl.notify(noteType="Incident",title=subject,description=message)

if __name__ == '__main__':
    Growlerduty().run()
