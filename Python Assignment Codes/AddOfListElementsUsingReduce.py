from functools import reduce

Addition = lambda No, No2 : No + No2

def main():

    Data = [1,2,3,4,5,6,7,8,9,10]

    RData = reduce(Addition, Data)

    print("Addition of list elements : ",RData)

if __name__ == "__main__":
    main()