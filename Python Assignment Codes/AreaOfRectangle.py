def AreaOfrectangle(Length, Width):
    return Length * Width

def main():
    l = int(input("Enter length of rectangle : "))
    w = int(input("Enter width of rectangle : "))

    Ret = AreaOfrectangle(l, w)

    print("Area of rectangle is : ",Ret)
if __name__ == "__main__":
    main()