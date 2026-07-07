import time
import multiprocessing
import os

def Prime(Data):

    count = 0

    for No in range(2, Data + 1):
    
        for i in range(2, No):
            if No % i  == 0:
                break

        else:
            count = count + 1

    return (os.getpid(), Data, count)
    
def main():

    Data = [10000, 20000, 30000, 40000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Prime, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    for pid, Data, count in Result:
        print(f"Process ID      : {pid}")
        print(f"Input Number    : {Data}")
        print(f"Prime numbers : {count}")
        print("-" * 60)

    print(f"\nTime required is {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()