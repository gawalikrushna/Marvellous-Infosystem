from functools import reduce

Check = lambda No : No % 2 == 0

Square = lambda No : No ** 2

Addition = lambda No1, No2 : No1 + No2

def main():
    No = int(input("How many elemetns yo want to enter in List : "))

    Data = []

    print("Enter elements : ")

    for i in range(No):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Check, Data))
    print("List after filter : ",FData)

    MData = list(map(Square, FData))
    print("List after map : ",MData)

    RData = reduce(Addition, MData)
    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()