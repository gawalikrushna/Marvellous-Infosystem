from functools import reduce

ChkMax = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    N = int(input("Input Elements : "))
    
    Data = []

    print("Enter the elements : ")

    for i in range(1, N + 1):
        Value = int(input())
        Data.append(Value)
    Ret = reduce(ChkMax, Data)
    
    print("Maximum number is : ",Ret)

if __name__ == "__main__":
    main()