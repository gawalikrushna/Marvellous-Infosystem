def main():

    FileName = input("Enter file name : ")

    fobj = open(FileName,"r")

    for line in fobj:
        print(line, end=" ")

    fobj.close()

if __name__ == "__main__":
    main()