#!/usr/bin/env python2 
from pync import Notifier
from pygermeister import PygerMeister

class Macerduty(PygerMeister):
    def __init__(self, confFile="~/.pygerrc"):
        PygerMeister.__init__(self,confFile)
        self.config = self.getConfig(confFile)

    def run(self):
        PygerMeister.run(self)

    def sendIncident(self,subject,message):
        if self.args.verbose:
            print "Sending incident popup (%s - %s)" % (subject,message)
        Notifier.notify(message, title=subject)


if __name__ == '__main__':
    Macerduty().run()
