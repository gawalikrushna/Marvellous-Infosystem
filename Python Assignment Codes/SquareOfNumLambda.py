Square = lambda No : No * No

def main():
    Value = int(input("Enter number : "))

    Ret = Square(Value)

    print(f"Square of {Value} is : ",Ret)

if __name__ == "__main__":
    main()