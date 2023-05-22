import pyvisa
import sys
import time
rm = pyvisa.ResourceManager()
class scoop(object):
    # TODO: error handeling beter op poten zetten+ visa instument list "variable maken
    def __init__(self,visaadder):
        self.visaInstrList= rm.list_resources()
        print(self.visaInstrList)
        if len(self.visaInstrList) == 0:
            print("ERROR: no instrument found!")
            print("Exited because of error.")
            sys.exit(1)
        myscope = self.visaInstrList[0]
        self.scope = rm.open_resource(visaadder)
        idn_string = self.scope.query("*IDN?")
        if len(idn_string) == 0:
            print("ERROR: no instrument found!")
            print("Exited because of error.")
            sys.exit(1)
        else:
            print("Identification string: '%s'" % idn_string)
        self.scope.timeout = 15000
    def autoscale(self):#autoscales the scoop trace on any channel
        self.scope.write(":AUT")
    def clearscoop(self):#clears the traces in single run mode from the display
        self.scope.write(":CLE")
    def scooprun(self):#sets the scope  in run mode
        self.scope.write(":RUN")
    def scoopstop(self):#sets the scope  in stop mode
        self.scope.write(":STOP")
    def singlecapture(self):
        self.scope.write(":SING")
    def forcetrigger(self):#only works in single or normal trigger mode
        self.scope.write(":TFOR")
    def aquirenrofavrages(self):
        avrages=self.scope.query(":ACQ:AVER?")
        return avrages
    def setnrofavrages(self,nr):
        # TODO write code to catch out of bound input
        self.scope.write(":ACQ:AVER %d"%nr)
    def aquirememdepth(self):
        memdepth = self.scope.query(":ACQ:MDEP?")
        return memdepth
    def setmemdepth(self,memmorydepth):
        # TODO write code to catch out of bound input
        self.scope.write(":ACQ:MDEP %s" % memmorydepth)
    def aquiretype(self):
        aquire = self.scope.query(":ACQ:TYPE?")
        return aquire
    def setaquiretype(self,type):
        # TODO write code to catch out of bound input
        self.scope.write(":ACQuire:TYPE %s" % type)





