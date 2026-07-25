import sys

def main():
    FileName = sys.argv[1]

    try:
        fobj = open(FileName,"r")
        Data = fobj.read()

        NewFile = open("Demo3.txt","w")
        NewFile.write(Data)

        fobj.close()
        NewFile.close()

        print(f"{FileName} is copied sucessfully in Demo3.txt")

    except FileNotFoundError as e:
        print("No such file in directory")

if __name__ == "__main__":
    main()