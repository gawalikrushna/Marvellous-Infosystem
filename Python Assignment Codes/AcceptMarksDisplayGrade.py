def main():
    C = int(input("Enter C language marks : "))
    OOP = int(input("Enter OOP marks : "))
    OS = int(input("Enter OS marks : "))
    DS = int(input("Enter DS language marks : "))
    CN = int(input("Enter CN marks : "))

    Marks = ((C + OOP + OS + DS + CN) * 100) / 500 

    print("Your percentage is : ",Marks)

    if Marks >= 75:
        print("Distinction")
    elif Marks >= 60:
        print("First class")
    elif Marks >= 50:
        print("Second class")
    else:
        print("Fail")


if __name__ == "__main__":
    main()