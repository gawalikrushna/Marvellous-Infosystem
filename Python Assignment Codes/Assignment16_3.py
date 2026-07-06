def ChkNUm(No1, No2):
    return No1 + No2

def main():

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = ChkNUm(Value1, Value2)

    print(f"Addition of {Value1} and {Value2} is : ",Ret)

if __name__ ==  "__main__":
    main()