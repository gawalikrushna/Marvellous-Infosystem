import threading
import time

def Thread1(No):

    print("1 - number : ")

    for i in range(1, No+1):
        print(i, end=" ")


def Thread2(No):

    print("\n\nNumber - 1 : ")

    for i in range(No, 0, -1):
        print(i, end=" ")


def main():

    No = int(input("Enter number : "))

    t1 = threading.Thread(target=Thread1, args=(No,))
    t2 = threading.Thread(target=Thread2, args=(No,))

    start_time = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"\n\nTime required is {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()