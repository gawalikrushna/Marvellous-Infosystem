def DisplayPattern():
    Value = int(input("Enter a number : "))

    for i in range(Value):
        for j in range(Value):

            print("*", end="  ")

        print()

if __name__ ==  "__main__":
    DisplayPattern()         