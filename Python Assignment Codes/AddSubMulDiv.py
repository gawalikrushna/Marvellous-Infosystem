def Add(No1,No2):
    return No1 + No2

def Sub(No1,No2):
    return No1 - No2

def Mul(No1,No2):
    return No1 * No2

def Div(No1,No2):
    if No2 == 0:
        return "Divide by zero error"
    else:
        return No1 / No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Addition = Add(Value1, Value2)
    Substraction = Sub(Value1, Value2)
    Multiplication = Mul(Value1, Value2)
    Division = Div(Value1, Value2)

    print("Addition is : ",Addition)
    print("Substraction is : ",Substraction)
    print("Multiplication is ",Multiplication)
    print("Division is : ",Division)



if __name__ == "__main__":
    main()