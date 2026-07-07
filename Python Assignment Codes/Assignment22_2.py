import time
import multiprocessing
import os

def Factorial(Data):

    fact = 1

    for i in range(1, Data + 1):
        fact = fact * i

    return (os.getpid(), Data, fact)

def main():

    Data = [10,15,20,25]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    for pid, Data, fact in Result:
        print(f"Process ID      : {pid}")
        print(f"Input Number    : {Data}")
        print(f"Factorial is : {fact}")
        print("-" * 60)

    print(f"\nTime required is {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()