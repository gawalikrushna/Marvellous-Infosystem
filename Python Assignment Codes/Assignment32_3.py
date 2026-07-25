import schedule
import time

def ReadFile(FilePath):

    try:
        fobj = open(FilePath,"r")
        Data = fobj.read()

        if Data == "":
            print("File is empty")
        else:
            print("\nFile contents : ")
            print(Data)

        fobj.close()

    except FileNotFoundError:
        print("File does not exists")

    except PermissionError:
        print("Permission is denied")

    except OSError:
        print("File cannot be opened")

def main():
    FilePath = input("Enter file path : ")

    schedule.every(5).seconds.do(ReadFile, FilePath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()