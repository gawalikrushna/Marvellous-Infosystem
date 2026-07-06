def DisplayNumbers():
    Value = int(input("Enter a number : "))

    for i in range(1,Value + 1):
        for j in range(1, i + 1):

            print(j, end="  ")

        print()

if __name__ ==  "__main__":
    DisplayNumbers()