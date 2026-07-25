import time
import datetime
import schedule

def NewFileCreation():
    CurrentTime = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    FileName = f"File_{CurrentTime}.txt"

    fobj = open(FileName,"w")
    fobj.write(f"File Name : {FileName}\n")
    fobj.write(f"Creation date : {datetime.date.today()}\n")
    fobj.write(f"Creation time : {datetime.datetime.now().strftime('%H:%M:%S')}\n")

    fobj.close()

    print(f"File Sucessfully created : {FileName}")

def main():
    schedule.every(3).seconds.do(NewFileCreation)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()