def main():
    Num = int(input("Enter number : "))
    fact = 1

    for i in range(1, Num + 1):
        fact = fact * i

    print(f"Factorial of {Num} is : ",fact)

if __name__ == "__main__":
    main()