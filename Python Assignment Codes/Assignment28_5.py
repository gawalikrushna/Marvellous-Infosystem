def main():
    FileName = input("Enter name of file : ")
    SearchWord = input("Enter word for sraching : ")

    fobj = open(FileName,"r")
    Data = fobj.read()

    if  SearchWord in Data:
        print(f"{SearchWord} is present in {FileName}")

    else:
        print(f"{SearchWord} is not present in {FileName}")

    fobj.close()
if __name__ == "__main__":
    main()
    