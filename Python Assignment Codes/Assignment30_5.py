import time,schedule,datetime

def Display():

    fobj = open("Marvellous.txt","a")
    fobj.write(f"Task executed at : {datetime.datetime.now()}\n")

    fobj.close()

def main():
    schedule.every(5).minutes.do(Display)

    while  True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__": 
    main()