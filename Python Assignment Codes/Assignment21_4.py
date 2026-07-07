import threading
import time
from functools import reduce

Sumation = lambda No1, No2 : No1 + No2

Product = lambda No1, No2 : No1 * No2

def SumThread(Data, Result):
    Result.append(reduce(Sumation, Data))

def ProductThread(Data, Result):
    Result.append(reduce(Product, Data))


def main():

    No = int(input("How many elements you want to enter in list : "))

    Data = []

    print("Enter elements : ")

    for i in range(No):
        Value =  int(input())
        Data.append(Value)

    SumResult = []
    ProductResult = []

    t1 = threading.Thread(target=SumThread, args=(Data, SumResult,))
    t2 = threading.Thread(target=ProductThread, args=(Data, ProductResult,))

    start_time = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print("\nSumation is : ",SumResult [0])

    print("Product is : ",ProductResult [0])

    print(f"\n\nTime required is {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()