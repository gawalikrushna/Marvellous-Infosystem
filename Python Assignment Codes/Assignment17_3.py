def Factorial(No):
    fact = 1

    for i in range(1,No + 1):
        fact = fact * i

    return fact

def main():
    Value = int(input("Enter a number : "))

    Ret = Factorial(Value)

    print(f"Factorial of {Value} is : ",Ret)


if __name__ ==  "__main__":
    main()     