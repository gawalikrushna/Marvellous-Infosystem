def PrimeNumber(No):
    if No % 2 != 0:
        return True
    
    else:
        return False

def main():
    Value = int(input("Enter a number : "))

    Ret = PrimeNumber(Value)

    if Ret == True:
        print("Its prime number")

    else:
        print("Its not prime")



if __name__ ==  "__main__":
    main()         