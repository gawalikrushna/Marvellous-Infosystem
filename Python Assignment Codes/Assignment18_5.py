import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for i in Data:
        if MarvellousNum.ChkPrime(i):
            Sum = Sum + i

    return Sum

def main():
    N = int(input("Input Elements : "))
    
    Data = []

    print("Enter the elements : ")

    for i in range(1, N + 1):
        Value = int(input())
        Data.append(Value)

    Ret = ListPrime(Data)

    print("Sumation of prime numbers is : ",Ret)


if __name__ == "__main__":
    main()