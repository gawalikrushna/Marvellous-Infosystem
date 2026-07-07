from functools import reduce

def Check(No):
    if No <= 1:
        return False
    for i in range(2, No): 
        if No % i == 0:
            return False
        
    return True

Multiply = lambda No : No * 2

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2 

def main():
    No = int(input("How many elements yo want to enter in List : "))

    Data = []

    print("Enter elements : ")

    for i in range(No):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Check, Data))
    print("List after filter : ",FData)

    MData = list(map(Multiply, FData))
    print("List after map : ",MData)

    RData = reduce(Maximum, MData)
    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()