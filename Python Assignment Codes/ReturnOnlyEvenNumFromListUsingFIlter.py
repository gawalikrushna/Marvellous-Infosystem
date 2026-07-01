CheckEven = lambda No : No % 2 == 0

def main():

    Data = [1,2,3,4,5,6,7,8,9,10]

    FData = list(filter(CheckEven, Data))

    print("Even elements from Data : ",FData)

if __name__ == "__main__":
    main()