import threading
import time

Counter = 0
Lock = threading.Lock()

def Increment():
    global Counter

    for i in range(5000000):
        with Lock:
            Counter += 1

def main():

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)
    t3 = threading.Thread(target=Increment)

    ST = time.perf_counter()

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    ET = time.perf_counter()

    print("Final value of Counter is :", Counter)

    print(f"\nTime required is {ET - ST:.5f} seconds")

if __name__ == "__main__":
    main()