import multiprocessing
import time
import os

def SumOfOdd(Data):

    Ret = 0

    for i in range(1, Data + 1):
        if i % 2 != 0:
            Ret = Ret + i

    return (os.getpid(), Data, Ret)

def main():

    Data = [1000000,2000000,3000000,4000000]

    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOfOdd, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    for PID, Data, Ret in Result:
        print(f"Process ID      : {PID}")
        print(f"Input Number    : {Data}")
        print(f"Sum of odd numbers : {Ret}")
        print("-" * 60)        

    print(f"Time required is {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()

