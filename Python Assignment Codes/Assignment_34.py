import psutil
import sys
import os
import time 
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def ProcessScan():
    ListProcess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs = ["pid","name","username","status"])
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            ListProcess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return ListProcess

def ProcessDisplay(ProcessName):
    Found = False
    Border = "-"*50
    print(Border)
    print(f"Searching for process : {ProcessName}")
    print(Border)

    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == ProcessName.lower():
                Found = True
                info = proc.as_dict(attrs = ["pid","name","username","status"])
                print(f"PID : {info.get('pid')}")
                print(f"Name : {info.get('name')}")
                print(f"User Name : {info.get('username')}")
                print(f"Status : {info.get('status')}")
                print(Border)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if not Found:
        print(f"No active process found with name : {ProcessName}")

def SendMail(FileName, MailID):
    SenderEmail = "krushnag@2605@gmail.com"     
    SenderPassword = "nvgt szhj dwyd acqz"    

    try:
        msg = MIMEMultipart()
        msg['From'] = SenderEmail
        msg['To'] = MailID
        msg['Subject'] = "Marvellous Platform Surveillance System Log"

        body = "Hello,\n\nPlease find attached the process surveillance log file."
        msg.attach(MIMEText(body, 'plain'))

        if os.path.exists(FileName):
            with open(FileName, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(FileName)}")
                msg.attach(part)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SenderEmail, SenderPassword)
        server.send_message(msg)
        server.quit()

        print(f"Log file successfully sent to {MailID}")

    except Exception as err:
        print(f"Failed to send email : {err}")

def PlatformSurvillence(FolderName, MailID=None):
    Border = "-"*50

    Ret = os.path.exists(FolderName)

    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to proceed as directory name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created sucessfully")

    timestamp = time.strftime("%d_%m_%Y_%H_%M_%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)

    fobj = open(FileName, "w")

    print(f"Log file gets sucessfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("------Marvellous platform Survillence Systmem------\n")
    fobj.write(f"Log file gets created at : {timestamp}\n")
    fobj.write(Border+"\n\n")

    fobj.write("------------------System Report--------------------\n")

    #CPU Information
    fobj.write("Number of active CPU cores : %s \n"%psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n"%psutil.cpu_percent())
    fobj.write(Border+"\n")

    # RAM Information
    Memory = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n"%Memory.percent)
    fobj.write("Total RAM available : %s\n"%Memory.total)
    fobj.write(Border+"\n")

    # Network Usage
    Netobj = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(Netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(Netobj.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # Process log
    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n"%info.get("pid"))
        fobj.write("Name : %s\n"%info.get("name"))
        fobj.write("User Name : %s\n"%info.get("username"))
        fobj.write("Status : %s\n"%info.get("status"))
        fobj.write("CPU Usage : %.2f\n"%info.get("cpu_percent"))
        fobj.write("RAM Usage: %.2f\n"%info.get("memory_percent"))
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("-----------------End of Log File-------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

    if MailID:
        SendMail(FileName, MailID)

def main():
    Border = "-"*50
    print(Border)
    print("------Marvellous platform Survillence Systmem------")
    print(Border)

    if(len(sys.argv) == 1):
        Data = ProcessScan()
        for info in Data:
            print(f"PID : {info.get('pid')} | Name : {info.get('name')} | User : {info.get('username')}")

    elif(len(sys.argv) == 2):
        if(sys.argv[1].lower() in ["--h", "-h"]):
            print("This automation script is used to perform:")
            print("1 : Fetch information of running processes")
            print("2 : Search specific running process")
            print("3 : Maintain process logs in folder")
            print("4 : Mail log reports periodically")

        elif(sys.argv[1].lower() in ["--u", "-u"]):
            print("Usage examples:")
            print(f"  1. Display all processes : python {sys.argv[0]}")
            print(f"  2. Search process        : python {sys.argv[0]} ProcessName")
            print(f"  3. Create process log    : python {sys.argv[0]} DirectoryName")
            print(f"  4. Log & mail report     : python {sys.argv[0]} DirectoryName EmailID")
            print(f"  5. Schedule log & mail   : python {sys.argv[0]} Time_Interval DirectoryName [EmailID]")

        else:
            if os.path.exists(sys.argv[1]) and os.path.isdir(sys.argv[1]):
                PlatformSurvillence(sys.argv[1])
            else:
                ProcessDisplay(sys.argv[1])

    elif(len(sys.argv) == 3):
        if sys.argv[1].isdigit():
            print("Scheduler started sucessfully....")
            print("Press Ctrl + C to abort the automation script")
            schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2])
            
            try:
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nScript execution aborted.")
                return
        else:
            PlatformSurvillence(sys.argv[1], sys.argv[2])

    elif(len(sys.argv) == 4):
        if sys.argv[1].isdigit():
            print("Scheduler started sucessfully....")
            print("Press Ctrl + C to abort the automation script")
            
            PlatformSurvillence(sys.argv[2], sys.argv[3])
            
            schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2], sys.argv[3])
            
            try:
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nScript execution aborted.")
                return

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("------Thanku for using our automation system------")
    print("------Marvellous platform Survillence Systme------")
    print(Border)

if __name__ == "__main__":
    main()