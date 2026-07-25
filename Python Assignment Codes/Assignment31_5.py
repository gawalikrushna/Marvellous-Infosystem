import schedule
import time
import datetime
import os

def CountFiles(DirectoryPath):

    if not os.path.isdir(DirectoryPath):
        print("Directory does not exist.")
        return

    FCount = 0

    for Root, Directories, Files in os.walk(DirectoryPath):
        FCount += len(Files)

    with open("DirectoryCountLog.txt", "a") as fobj:
        fobj.write(f"Directory Path : {DirectoryPath}\n")
        fobj.write(f"Number of Files : {FCount}\n")
        fobj.write(f"Date And Time : {datetime.datetime.now()}\n")
        fobj.write("---------------------------------\n")

        fobj.close()

    print("Log updated successfully.")

def main():

    DirectoryPath = input("Enter Directory Path : ")

    schedule.every(5).minutes.do(CountFiles, DirectoryPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()