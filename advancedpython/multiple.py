class Village:
    villagename = "Palakkad"

    def family1(self, members):
        self.members = members
class Town :
    def detailtown(self):
        print("second inheritence")



class Panchayat(Village,Town):
    def detail(self):
        print("village name", Village.villagename)
        print("family1", self.members)



o1 = Panchayat()
o1.family1(5)
o1.detail()
o1.detailtown()
