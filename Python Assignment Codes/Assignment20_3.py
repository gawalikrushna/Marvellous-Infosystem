import time
import threading

def EvenList(No):
    Even = []
    Sum = 0

    for i in No:
        if i % 2 == 0:
            Even.append(i)
            Sum = Sum + i

    print("Even list : ",Even)
    print("Sumation of even list : ",Sum)

def OddList(No):
    Odd = []
    Sum = 0

    for i in No:
        if i % 2 != 0:
            Odd.append(i)
            Sum = Sum + i

    print("Odd list : ",Odd)
    print("Sumation of odd list : ",Sum)

def main():

    No = int(input("How many elements you want to enter in list : "))

    Data = []

    print("Enter elements : ")

    for i in range(No):
        Value = int(input())
        Data.append(Value)


    start_time = time.perf_counter()

    t1 = threading.Thread(target=EvenList, args=(Data,))

    t2 = threading.Thread(target=OddList, args=(Data,))

    end_time = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"\nTime required is {end_time - start_time:.5f} seconds")


if __name__ == "__main__":
    main()
