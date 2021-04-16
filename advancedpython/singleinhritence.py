class Village :
     villagename = "Palakkad"
     def family1(self,members):
          self.members = members
class Panchayat(Village):
     def detail(self):
       print("village name",Village.villagename)
       print("family1",self.members)
o1 = Panchayat()
o1.family1(5)
o1.detail()

