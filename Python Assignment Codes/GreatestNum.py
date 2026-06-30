def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter first number : "))

    if Num1 > Num2 :
        print(f"{Num1} is greater number")
    elif Num1 < Num2:
        print(f"{Num2} is greater number")
    else:
        print("Both numbers are equal")

if __name__ == "__main__":
    main()