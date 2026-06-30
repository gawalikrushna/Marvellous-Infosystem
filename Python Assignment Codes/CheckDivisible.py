def CheckDivisible(No):
    if No % 3 == 0 and No % 5 == 0:
        return True
    else:
        return False

def main():

    Num = int(input("Enter number : "))

    Ret = CheckDivisible(Num)

    if Ret == True:
        print(f"{Num} is divisible by 3 and 5")
    else:
        print(f"{Num} is not divisible by 3 and 5")

if __name__ == "__main__":
    main()