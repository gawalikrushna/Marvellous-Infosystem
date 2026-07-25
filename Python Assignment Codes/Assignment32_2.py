import os 
import schedule
import time
import datetime

def FileSize(FilePath):

    if not os.path.isfile(FilePath):
        print("File does not exists")
        return

    Size = os.path.getsize(FilePath)

    fobj = open("FileSizeLog.txt","a")
    fobj.write(f"File path : {FilePath}\n")
    fobj.write(f"File size : {Size} bytes\n")
    fobj.write(f"Date and time : {datetime.datetime.now()}\n")
    fobj.write("-----------------------------------------------------\n")

    fobj.close()

def main():
    FilePath = input("Enter file path : ")

    schedule.every(5).seconds.do(FileSize, FilePath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()