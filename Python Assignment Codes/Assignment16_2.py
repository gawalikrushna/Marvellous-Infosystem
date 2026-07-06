def ChkNUm(No):
    if No % 2 == 0:
        return True
    else:
        return False

def main():

    Value = int(input("Enter a number : "))

    Ret = ChkNUm(Value)

    if Ret == True:
        print("Even number")
    else:
        print("Odd number")

if __name__ ==  "__main__":
    main()