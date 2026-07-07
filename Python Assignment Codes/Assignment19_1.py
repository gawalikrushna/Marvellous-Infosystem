Power = lambda No : No ** 2

def main():
    Value = int(input("Enter number : "))

    Ret = Power(Value)

    print(f"Power of {Value} is : ",Ret)

if __name__ == "__main__":
    main()