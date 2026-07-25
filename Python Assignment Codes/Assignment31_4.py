import time
import schedule
import datetime

def CreateLog():
    timestamp = time.ctime()
    LogFileName = "Marevellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj = open(LogFileName,"w")
    fobj.write("Log file created sucessfully\n")
    fobj.write(f"Creation Time : {datetime.datetime.now()}")

    fobj.close()


def main():
    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)    

if __name__ == "__main__":
    main()
