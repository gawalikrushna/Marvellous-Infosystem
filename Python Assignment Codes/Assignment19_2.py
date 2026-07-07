Multiplication = lambda No1, No2 : No1 * No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Multiplication(Value1, Value2)

    print(f"Multiplication of {Value1} and {Value2} is : ",Ret)

if __name__ == "__main__":
    main()