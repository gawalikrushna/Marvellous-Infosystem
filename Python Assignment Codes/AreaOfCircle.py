def AreaOfCircle(Redius, PI = 3.14):
    return PI * Redius * Redius

def main():
    R = int(input("Enter redius of circle : "))

    Ret = AreaOfCircle(R)

    print("Area of circle is : ",Ret)
if __name__ == "__main__":
    main()