class College:
    collegename = "CEM"
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def printdetail(self):
        print("college",self.collegename)
        print("name",self.name)
        print("roll",self.roll)
    def __str__(self):
        return self.name + str(self.roll)

o1 = College("ani",41)
print(o1)