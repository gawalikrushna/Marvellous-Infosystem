def main():

    Source = input("Enter existing file name : ")
    Destination =  input("Enter destination file name : ")

    fsrc = open(Source,"r")
    fdest = open(Destination,"w")

    Data = fsrc.read()
    fdest.write(Data)

    print("Contents of", Source, "copied into", Destination)

    fsrc.close()
    fdest.close()

if __name__ == "__main__":
    main()