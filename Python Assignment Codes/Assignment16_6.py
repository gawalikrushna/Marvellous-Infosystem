def CheckNum():
    Num = int(input("Enter a number : "))

    if Num < 1 and Num > -1 :
        print("Number is zero")

    elif Num > 0 :
        print("Positive number")

    else:
        print("Negative number")

if __name__ ==  "__main__":
    CheckNum()