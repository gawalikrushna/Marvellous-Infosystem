def main():
    Num = int(input("Enter number : "))

    print(f"Multiplication table of {Num} is : ")

    for i in range(1, 11):
        print(Num * i)
        

if __name__ == "__main__":
    main()