#a child class Bus that will inherit all of the variables and methods of Vehicle
# class?
class Vehicle:
    vechiclecompany = "TVS"

    def vhdetail (self, vhmass,vhspeed,vhpower):
        self.vhmass = vhmass
        self.vhspeed = vhspeed
        self.vhpower = vhpower


class Bus(Vehicle):

    def busdetail(self,busname):
        self.busname = busname
        print("vhmass = ",self.vhmass)
        print("vhspeed = ",self.vhspeed)
        print("vhpower = ",self.vhpower)
        print("busname = ",self.busname)


o1 = Bus()
o1.vhdetail(2605,120,160)
o1.busdetail("srm")