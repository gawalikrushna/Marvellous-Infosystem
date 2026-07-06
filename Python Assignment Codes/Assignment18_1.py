def Sum(No):
    Sum = 0
    for i in No:
        Sum = Sum + i

    return Sum

def main():
    N = int(input("Input Elements : "))
    
    Data = []

    print("Enter the elements : ")

    for i in range(1, N + 1):
        Value = int(input())
        Data.append(Value)
    Ret = Sum(Data)
    
    print("Addition of list elements is : ",Ret)

if __name__ == "__main__":
    main()