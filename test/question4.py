#Create an Animal class using constructor and build a child class for Dog?
class Animal:
    def __init__(self,sound):
        self.sound = sound

class Dog(Animal):
    def __init__(self,sound,typ):
        super().__init__(sound)
        self.typ = typ
        print(self.sound,self.typ)
d = Dog("sound","bark")
