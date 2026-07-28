import sys
import os
import hashlib
import datetime
import smtplib
from email.message import EmailMessage

def CalculateChecksum(Filename):
    with open(Filename, "rb") as fobj:
        hobj = hashlib.md5()

        Buffer = fobj.read(1024)

        while len(Buffer) > 0:
            hobj.update(Buffer)
            Buffer = fobj.read(1024)

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    if os.path.exists(DirectoryName) == False:
        print("Path is invalid")
        return None

    if os.path.isdir(DirectoryName) == False:
        print("It is not a directory")
        return None

    Duplicate = {}

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName, fname)

            try:
                CheckSum = CalculateChecksum(fname)

                if CheckSum in Duplicate:
                    Duplicate[CheckSum].append(fname)
                else:
                    Duplicate[CheckSum] = [fname]

            except Exception:
                pass

    return Duplicate

def SendMail(LogFile,StartTime,EndTime,DirectoryName,TotalFiles,DuplicateFiles,DeletedFiles):

    SenderEmail = "krushnag2605@gmail.com"

    Password = "nvgt szhj dwyd acqz"

    ReceiverEmail = "gkrushna893@gmail.com"

    Body = f"""Jay Ganesh,

The duplicate-file removal operation has been completed successfully.

Operation Statistics:

Starting time of scanning : {StartTime}
Completion time of scanning : {EndTime}
Directory scanned : {DirectoryName}
Total number of files scanned : {TotalFiles}
Total number of duplicate files found : {DuplicateFiles}
Total number of duplicate files deleted : {DeletedFiles}

Please find the detailed log file attached to this email.

Regards,
Marvellous Automation System
"""

    try:
        msg = EmailMessage()

        msg["Subject"] = "Duplicate File Removal Report"
        msg["From"] = SenderEmail
        msg["To"] = ReceiverEmail

        msg.set_content(Body)

        with open(LogFile, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(LogFile)
            )

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        smtp.login(SenderEmail, Password)

        smtp.send_message(msg)

        smtp.quit()

        print("Mail Sent Successfully")

    except Exception as e:
        print("Unable to send mail :", e)

def DeleteDuplicate(DirectoryName):

    StartTime = datetime.datetime.now()

    MyDict = FindDuplicate(DirectoryName)

    if MyDict == None:
            return

    TotalFiles = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        TotalFiles = TotalFiles + len(FileName)

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    if os.path.exists("Marvellous") == False:
        os.mkdir("Marvellous")

    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    LogFile = os.path.join("Marvellous", "Log_" + timestamp + ".txt")

    with open(LogFile, "w") as fobj:

        fobj.write("Duplicate File Removal Log\n\n")
        fobj.write("Date and Time : " + str(datetime.datetime.now()) + "\n\n")

        Count = 0
        TotalDeleted = 0
        TotalGroups = len(Result)

        for Value in Result:

            Count = 0

            for subvalue in Value:

                Count += 1

                if Count > 1:

                    fobj.write("Deleted : " + subvalue + "\n")

                    try:
                        os.remove(subvalue)
                        TotalDeleted += 1

                    except Exception as e:
                        print(f"Error processing {FileName}: {e}")

        fobj.write("\n")
        fobj.write("Duplicate Groups : " + str(TotalGroups) + "\n")
        fobj.write("Deleted Files : " + str(TotalDeleted) + "\n")

    print("Total Deleted Files :", TotalDeleted)
    print("Log File Created :", LogFile)

    EndTime = datetime.datetime.now()

    DuplicateFiles = TotalDeleted
    DeletedFiles = TotalDeleted

    SendMail(LogFile, StartTime, EndTime, DirectoryName, TotalFiles, DuplicateFiles, DeletedFiles)

def main():

    if len(sys.argv) != 2:
        print("Usage : python Duplicate.py DirectoryName")
        return

    DeleteDuplicate(sys.argv[1])

if __name__ == "__main__":
    main()