def main():
    num = int(input("Enter number : "))

    print("Odd numbers are : ")

    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i)

if __name__ == "__main__":
    main()