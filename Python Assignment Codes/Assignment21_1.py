import threading
import time

def Prime(Data):

    Prime = []

    for No in Data:
        if No <= 1:
            continue
    
        for i in range(2, No):
            if No % i == 0:
                break
        else:
            Prime.append(No)

    print("Prime numbers list is : ",Prime)
        

def NonPrime(Data):

    Non_Prime = []

    for No in Data:
        if No <= 1:
            Non_Prime.append(No)
            continue
    
        for i in range(2, No):
            if No % i == 0:
                Non_Prime.append(No)
                break
        
    print("\nNon prime numbers list is : ",Non_Prime)


def main():

    No = int(input("How many elements you want to enter in list : "))

    Data = []

    print("Enter elements : ")

    for i in range(No):
        Value =  int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NonPrime, args=(Data,))

    start_time = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"\n\nTime required is {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()