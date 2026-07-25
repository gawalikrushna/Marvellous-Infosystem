def main():
    FileName = input("Enter file name : ")
    Str = input("Enter string for frequency count : ")

    fobj = open(FileName,"r")
    Data = fobj.read()

    Count = Data.count(Str)

    print("Frequency of string : ",Count) 

    fobj.close()

if __name__ == "__main__":
    main()