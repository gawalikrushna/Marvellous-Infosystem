import threading
import time
from functools import reduce


Maximum = lambda No1, No2 : No1 if No1 > No2 else No2
        
Minimum = lambda No1, No2 : No1 if No1 < No2 else No2 

def MaxThread(Data):
    print("Maximum element is :", reduce(Maximum, Data))

def MinThread(Data):
    print("Minimum element is :", reduce(Minimum, Data))


def main():

    No = int(input("How many elements you want to enter in list : "))

    Data = []

    print("Enter elements : ")

    for i in range(No):
        Value =  int(input())
        Data.append(Value)

    t1 = threading.Thread(target=MaxThread, args=(Data,))
    t2 = threading.Thread(target=MinThread, args=(Data,))

    start_time = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"\n\nTime required is {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()