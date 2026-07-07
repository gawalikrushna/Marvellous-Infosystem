import time
import threading

def Small(Str):

    S = 0
    for char in Str:
        if 'a' <= char <= 'z':
            S += 1

    print(f"""
Name of thread is : {threading.current_thread().name}
TID of Small thread is : {threading.get_ident()}
Small characters count is : {S}
""")
    
def Capital(Str):

    C = 0
    for char in Str:
        if 'A' <= char <= 'Z':
            C += 1

    print(f"""
Name of thread is : {threading.current_thread().name}
TID of Capital thread is : {threading.get_ident()}
Capital characters count is : {C}
""")

def Digits(Str):

    D = 0
    for char in Str:
        if '0' <= char <= '9':
            D += 1

    print(f"""
Name of thread is : {threading.current_thread().name}
TID of Digits thread is : {threading.get_ident()}
Digits count is : {D}
""")
    
def main():
    Char = input("Enter string : ")

    start_time = time.perf_counter()

    t1 = threading.Thread(target=Small, args=(Char,), name="Small")
    t2 = threading.Thread(target=Capital, args=(Char,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(Char,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end_time = time.perf_counter()

    print("Name of thread is :", threading.current_thread().name)
    print("TID of Main thread is :", threading.get_ident())

    print(f"\nTime required is : {end_time - start_time:.5f} seconds")


if __name__ == "__main__":
    main()