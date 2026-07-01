from functools import reduce

Product = lambda No1, No2 : No1 * No2 

def main():

    Data = [1,2,3,4,5]
    
    RData = reduce(Product, Data)

    print("Product of all elements is : ",RData)

if __name__ == "__main__":
    main()