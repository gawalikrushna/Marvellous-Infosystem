def RevNum():
    Num = int(input("Enter a numnber : "))
    rev = 0

    while Num > 0:
        ld = Num % 10
        rev = rev * 10 + ld
        Num = Num // 10

    print("Reverse of the number : ",rev)

if __name__ == "__main__":
    RevNum()