import time
import multiprocessing

def SumSquare(Data):

    S = 0 

    for i in range(1, Data + 1):
        if i % 2 == 0:
            S = S + i

    return S

def main():

    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is  : ")
    print(Result)

    print(f"Time required is {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()