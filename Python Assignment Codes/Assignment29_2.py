def main():
    try:
        FileName = input("Enter file name : ")

        fobj = open(FileName,"r")

        Data = fobj.read()

        print("File content : ")
        print(Data)

        fobj.close()

    except FileNotFoundError as e:
        print("No such file available in directory")

if __name__ == "__main__":
    main()