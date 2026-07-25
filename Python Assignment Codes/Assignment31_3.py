import schedule
import time
import datetime
import os

def DirectoryScanner(DirectoryPath):

    FCount = 0
    DCount = 0

    for Directory, SubDirectory, Files in os.walk(DirectoryPath):
        FCount += len(Files)
        DCount += len(SubDirectory)

    print("\nDirectory Scanned : ",DirectoryPath)
    print("Number of Files : ",FCount)
    print("Number of subdirectory : ",DCount)
    print("Scan Time : ",datetime.datetime.now())

def main():
    DirectoryPath = input("Enter Directory Path : ")

    schedule.every(1).minutes.do(DirectoryScanner, DirectoryPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


