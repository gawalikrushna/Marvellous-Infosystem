def Digits():
    num = int(input("Enter number : "))
    count = 0

    while num > 0:
        count = count + 1
        num = num // 10
    
    print("Digits in number are : ",count)

if __name__ == "__main__":
    Digits()
