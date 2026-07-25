import os
import time
import datetime
import schedule

def DeleteEmptyFiles(DirectoryPath):

    if not os.path.isdir(DirectoryPath):
        print("Directory does not exist.")
        return

    for Root, Directories, Files in os.walk(DirectoryPath):

        for File in Files:

            FilePath = os.path.join(Root, File)

            try:
                if os.path.getsize(FilePath) == 0:

                    os.remove(FilePath)

                    fobj = open("DeletedFilesLog.txt", "a")
                    fobj.write(f"{FilePath} deleted at {datetime.datetime.now()}\n")
                    fobj.close()

                    print(File, "Deleted Successfully")

            except PermissionError:
                print("Permission Denied :", FilePath)

            except Exception as e:
                print("Error :", e)

def main():

    DirectoryPath = input("Enter Directory Path : ")

    schedule.every(5).seconds.do(DeleteEmptyFiles, DirectoryPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()