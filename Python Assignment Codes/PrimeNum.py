def main():
    num = int(input("Enter number : "))
    a = 0
    for i in range(2, num):
        if num % i == 0:
            a = 1

    if a != 0:
        print("Not number")

    else:
        print("Prime prime")

if __name__ == "__main__":
    main()