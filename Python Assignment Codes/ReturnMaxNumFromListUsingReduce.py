from functools import reduce

MaxNum = lambda No1, No2 : No1 if No1 > No2 else No2 

def main():

    Data = [1,2,3,4,55,6,7,8,9,60]
    
    RData = reduce(MaxNum, Data)

    print("Maximum number from list : ",RData)

if __name__ == "__main__":
    main()