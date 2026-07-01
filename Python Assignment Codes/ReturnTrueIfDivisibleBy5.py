DivisibleBy5 = lambda No : True if No % 5 == 0 else False

def main():
    Value = int(input("Enter number : "))

    Ret = DivisibleBy5(Value)

    print(Ret)

if __name__ == "__main__":
    main()