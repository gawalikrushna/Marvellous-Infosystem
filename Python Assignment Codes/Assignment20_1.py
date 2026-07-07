import time
import threading

def Even(No):
    print("Even numbers : ")

    for i in range(1,No+1):
        if i % 2 == 0:
            print(i, end=" ")

    

def Odd(No):
    print("\nOdd numbers : ")

    for i in range(1,No+1):
        if i % 2 != 0:
            print(i, end=" ")

    
        

def main():

    start_time = time.perf_counter()

    t1 = threading.Thread(target=Even, args=(20,))

    t2 = threading.Thread(target=Odd, args=(20,))

    end_time = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"\nTime required is {end_time - start_time:.5f} seconds")


if __name__ == "__main__":
    main()
