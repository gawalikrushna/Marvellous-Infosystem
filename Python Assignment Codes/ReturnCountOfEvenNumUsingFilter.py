CheckEvenCount = lambda No : No % 2 == 0

def main():

    Data = [1,2,3,4,5,6,7,8,9,10]

    FData = list(filter(CheckEvenCount, Data))

    Count = len(FData)

    print("Even elements from Data : ",FData)
    print("Even numbers count : ",Count)

if __name__ == "__main__":
    main()