MinNum = lambda No1, No2 : "Both numbers are equal" if No1 == No2 else No1 if No1 < No2 else No2

def main():

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = MinNum(Value1,  Value2)

    print("Minimum number is : ",Ret)

if __name__ == "__main__":
    main()