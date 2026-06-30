def Perfect():
    num = int(input("Enter number : "))
    sum = 0

    for i in range(1, num - 1):
        if num % i == 0:
            sum = sum + i

    if sum == num:
        print("Perfect number")

    else:
        print("Not perfect num")

if __name__ == "__main__":
    Perfect()