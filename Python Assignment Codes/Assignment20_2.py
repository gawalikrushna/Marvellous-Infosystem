import time
import threading

def EvenFactors(No):
    Sum = 0
    print("Even factors of number : ")

    for i in range(1,No+1):
        if i % 2 == 0 and No % i == 0:
            print(i, end=" ")
            Sum = Sum + i

    print("\nSumation of even factors : ",Sum)

    

def OddFactors(No):
    Sum = 0
    print("\nOdd factors of number : ")

    for i in range(1,No+1):
        if i % 2 != 0 and No % i == 0:
            print(i, end=" ")
            Sum = Sum + i

    print("\nSumation of Odd factors : ",Sum)

    
        

def main():

    start_time = time.perf_counter()

    t1 = threading.Thread(target=EvenFactors, args=(20,))

    t2 = threading.Thread(target=OddFactors, args=(20,))

    end_time = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"\nTime required is {end_time - start_time:.5f} seconds")

    print("\nExit from main")


if __name__ == "__main__":
    main()
