def main():

    FileName = input("Enter file name : ")

    fobj = open(FileName,"r")

    Data = fobj.read()

    Word = Data.split()

    print(f"Total numbers of word in {FileName} : ",len(Word))

    fobj.close()

if __name__ == "__main__":
    main()