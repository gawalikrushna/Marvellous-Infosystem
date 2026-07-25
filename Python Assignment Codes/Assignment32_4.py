import schedule
import time
import os
import shutil
import datetime

def CopyTestFile(SourceDir, DestinationDir):

    if not os.path.isdir(SourceDir):
        print("Sorce directory does not exists")
        return

    if not os.path.isdir(DestinationDir):
        print("Destination directory does not exists")
        return

    for FileName in os.listdir(SourceDir):

        if FileName.endswith(".txt"):
            SourcePath = os.path.join(SourceDir, FileName)
            DestinationPath = os.path.join(DestinationDir, FileName)

            try:
                shutil.copy2(SourcePath, DestinationPath)

                fobj = open("CopyLog.txt","a")
                fobj.write(f"{FileName} copied sucessfully at {datetime.datetime.now()}\n")

                print(FileName, "Copied Sucessfully")

            except Exception as e:
                fobj = open("CopyLog.txt","a")
                fobj.write(f"Failed to copy {FileName} : {e}\n")

                print("Failed to copy", FileName)
def main():
    SourceDir = input("Enter Source Directpry : ")
    DestinationDir = input("Enter Destination Directory : ")

    schedule.every(5).seconds.do(CopyTestFile, SourceDir, DestinationDir)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()