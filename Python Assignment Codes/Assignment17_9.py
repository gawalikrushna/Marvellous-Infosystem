def DigitsInNum(No):
    Count = 0
    
    while No > 0:
        No = No // 10
        Count = Count + 1

    return Count
def main():
    Value = int(input("Enter a number : "))

    Ret = DigitsInNum(Value)

    print(f"Number of digits in {Value} are : ",Ret)

if __name__ ==  "__main__":
    main()        