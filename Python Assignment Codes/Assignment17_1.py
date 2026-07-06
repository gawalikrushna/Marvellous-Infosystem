from Arithematic import *
def main():

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Addition = Add(Value1, Value2)
    print(f"Addition of {Value1} and {Value2} is : ",Addition)

    Substraction = Sub(Value1, Value2)
    print(f"Substraction of {Value1} and {Value2} is : ",Substraction)

    Multiplication = Mul(Value1, Value2)
    print(f"Multiplication of {Value1} and {Value2} is : ",Multiplication)

    Division = Div(Value1, Value2)
    print(f"Division of {Value1} and {Value2} is : ",Division)

if __name__ == "__main__":
    main()