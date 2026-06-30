def Factor():
    num = int(input("Enter number : "))

    for i in range(1,num + 1):
        if num % i == 0:
            print(i)

if __name__ == "__main__":
    Factor()