def main():

    FileName = input("Enter file name : ")

    fobj = open(FileName,"r")

    Lines = fobj.readlines()

    print(f"Total numbers of lines in {FileName} : ",len(Lines))

    fobj.close()

if __name__ == "__main__":
    main()