def DivisibleBy5(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    Num = int(input("Enter a number : "))

    Ret = DivisibleBy5(Num)
    print(Ret)

if __name__ ==  "__main__":
    main() 