class Demo:
    Value = 0

    # Constructor
    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    # Instance method Fun()
    def Fun(self):
        print("Inside fun")
        print("No1 = ",self.No1)
        print("No2 = ",self.No2)

    # Instance method Gun()
    def Gun(self):
        print("Inside gun")
        print("No1 = ",self.No1)
        print("No2 = ",self.No2)

dobj1 = Demo(11,21)
dobj2 = Demo(51,101)

dobj1.Fun()
dobj2.Fun()

dobj1.Gun()
dobj2.Gun()