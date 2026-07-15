class Circle:

    PI = 3.14

    def __init__(self):
        self.Redius = 0.0
        self.Redius = 0.0
        self.CircumFurance = 0.0

    def Accept(self):
        self.Redius = float(input("Enter redius : "))

    def CalArea(self):
        self.Area = Circle.PI * self.Redius * self.Redius

    def CalCircumFurance(self):
        self.CircumFurance = 2 * Circle.PI * self.Redius

    def Display(self):
        print("\nRedius = ",self.Redius)
        print("Area = ",self.Area)
        print("CircumFurance = ",self.CircumFurance) 

cobj1 = Circle()
cobj1.Accept()
cobj1.CalArea()
cobj1.CalCircumFurance()
cobj1.Display()

cobj2 = Circle()
cobj2.Accept()
cobj2.CalArea()
cobj2.CalCircumFurance()
cobj2.Display()