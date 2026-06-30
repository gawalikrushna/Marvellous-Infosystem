def RevNum():
    Num = int(input("Enter a number : "))
    newNum = Num
    Rev = 0

    while newNum > 0:
        ld = newNum % 10
        Rev = Rev * 10 + ld
        newNum = newNum // 10
    if Rev == Num:
        print(f"{Num} is palindrome")

    else:
        print(f"{Num} is not palindrome")

if __name__ == "__main__":
    RevNum()