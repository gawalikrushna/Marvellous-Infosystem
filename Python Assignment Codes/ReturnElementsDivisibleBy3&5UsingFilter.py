DivisibleBy3And5 = lambda No : No % 3 == 0 and No % 5 == 0

def main():

    Data = [15,2,19,3,12,29,5,23,30,6,45,20,8,9,10]

    FData = list(filter(DivisibleBy3And5, Data))

    print("List of numbers which is divisible by 3 and 5 : ",FData)

if __name__ == "__main__":
    main()