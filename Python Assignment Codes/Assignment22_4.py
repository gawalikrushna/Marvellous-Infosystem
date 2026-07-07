import time
import multiprocessing
import os

def SumOfPowerFive(Data):

    Ret = 0

    for i in range(1, Data+1):
        Ret = Ret + (i ** 5)

    return (os.getpid(), Data, Ret)
    
def main():

    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOfPowerFive, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    for pid, num, Ret in Result:
        print(f"Process ID      : {pid}")
        print(f"Input Number    : {num}")
        print(f"Sum of 5th Power: {Ret}")
        print("-" * 60)

    print(f"\nTime required is {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()