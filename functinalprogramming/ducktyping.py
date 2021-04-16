class Pycharm :
    def open(self):
        print("self pycharm")
    def run(self):
        print("print pycharm run")
    def debugg(self):
        print("debug pycharm")
class Vscode :
    def open(self):
        print("vs code open")
    def run (self):
        print("vs code run")

    def debugg(self):
        print("debug vscode")
class Programmer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debugg()
p1 = Pycharm()
p2 = Vscode()
p3 = Programmer()
p3.coding(p1)
p3.coding(p2)