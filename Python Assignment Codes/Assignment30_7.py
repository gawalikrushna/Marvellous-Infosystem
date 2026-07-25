import time
import datetime
import schedule
import shutil
import os

def Backup(Source, Destination):

    if not os.path.isfile(Source):
        print("Error: Source file does not exist.")
        return

    if not os.path.isdir(Destination):
        print("Error: Destination directory does not exist.")
        return

    FileName = os.path.basename(Source)
    name, ext = os.path.splitext(FileName)

    CurrentTime = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    BackupFileName = f"{name}_{CurrentTime}{ext}"

    BackupPath = os.path.join(Destination, BackupFileName)

    shutil.copy2(Source, BackupPath)

    with open("Backup_log.txt", "a") as fobj:
        fobj.write(f"Backup completed successfully at {datetime.datetime.now()}\n")

    print("Backup created successfully.")

def main():

    Source = input("Enter source file path: ")
    Destination = input("Enter destination folder path: ")

    schedule.every(1).hours.do(Backup, Source, Destination)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()