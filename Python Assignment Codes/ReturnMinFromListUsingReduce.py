from functools import reduce

MiniMum = lambda No1, No2: No1 if No1 < No2 else No2  

def main():

    Data = [3,4,55,7,8,9,2,10]
    RData = reduce(MiniMum, Data)

    print("Minimum num from list : ",RData)

if __name__ == "__main__":
    main()