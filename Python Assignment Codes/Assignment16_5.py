def Num():
    Value = int(input("Enter a number : "))

    for i in range(Value, 0, -1):
        print(i, end=" ")

if __name__ ==  "__main__":
    Num()