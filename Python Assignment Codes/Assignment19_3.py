from functools import reduce

Check = lambda No : No >= 70 and No <= 90 

Add = lambda No : No + 10

Product = lambda No1, No2 : No1 * No2

def main():
    No = int(input("How many elemetns yo want to enter in List : "))

    Data = []

    print("Enter elements : ")

    for i in range(No):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Check, Data))
    print("List after filter : ",FData)

    MData = list(map(Add, FData))
    print("List after map : ",MData)

    RData = reduce(Product, MData)
    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()