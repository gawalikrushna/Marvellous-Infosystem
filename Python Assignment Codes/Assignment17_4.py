def SumFactors(No):
    Add= 0

    for i in range(1,No):
        if No % i == 0:
            Add = Add + i

    return Add

def main():
    Value = int(input("Enter a number : "))

    Ret = SumFactors(Value)

    print(f"Factorial of {Value} is : ",Ret)


if __name__ ==  "__main__":
    main()


          