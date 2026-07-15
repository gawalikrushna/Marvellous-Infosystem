class Arithemetic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter 1st number : "))
        self.Value2 = int(input("Enter 2nd number : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError:
            return "Unable to divide by zero"

Aobj1 = Arithemetic()
Aobj2 = Arithemetic()

Aobj1.Accept()
print("\nAddition is : ",Aobj1.Addition())
print("Substraction is : ",Aobj1.Substraction())
print("Multiplication is : ",Aobj1.Multiplication())
print("Division is : ",Aobj1.Division())

Aobj2.Accept()
print("\nAddition is : ",Aobj2.Addition())
print("Substraction is : ",Aobj2.Substraction())
print("Multiplication is : ",Aobj2.Multiplication())
print("Division is : ",Aobj2.Division())