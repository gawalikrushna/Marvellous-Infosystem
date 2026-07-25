import sys

def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    try:
        fobj = open(FileName1,"r")
        fobj1 = open(FileName2,"r")

        Data1 = fobj.read()
        Data2 = fobj1.read()

        if Data1 == Data2:
            print("Sucess")
        else:
            print("Failure")

        fobj.close()
        fobj1.close()

    except FileNotFoundError as e:
        print("No such file in directory")

if __name__ == "__main__":
    main()