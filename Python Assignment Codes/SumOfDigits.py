def Digits():
    num = int(input("Enter number : "))
    sum = 0

    while num > 0:
        ld = num % 10
        sum = sum + ld
        num = num // 10
    
    print("Sum of Digits is  : ",sum)

if __name__ == "__main__":
    Digits()
