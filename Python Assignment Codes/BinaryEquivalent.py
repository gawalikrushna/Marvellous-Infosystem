def BinaryEquivalent():

    num = int(input("Enter number : "))
    Bin = 0
    pow = 0

    while num > 0:
        rem = num % 2
        Bin = Bin + (rem * (10 ** pow))
        pow = pow + 1
        num = num // 2

    print("Binary equivalent is : ",Bin)

if __name__ == "__main__":
    BinaryEquivalent()