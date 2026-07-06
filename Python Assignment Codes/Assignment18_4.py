from functools import reduce

def FrequencyOfNum(Data, Num):
    Count = 0

    for i in (Data):
        if i == Num:
            Count = Count + 1

    return Count

def main():
    N = int(input("Input Elements : "))
    
    Data = []

    print("Enter the elements : ")

    for i in range(1, N + 1):
        Value = int(input())
        Data.append(Value)

    Num = int(input("Enter element for search : "))

    Ret = FrequencyOfNum(Data, Num)
    
    print("Frequency of number is : ",Ret)

if __name__ == "__main__":
    main()