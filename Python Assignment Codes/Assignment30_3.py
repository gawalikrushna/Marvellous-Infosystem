import time,schedule

def Display():
    print("Coding Kar..!")

def main():
    schedule.every(30).minutes.do(Display)

    while  True:
        schedule.run_pending()
        time.sleep(3)

if __name__ == "__main__": 
    main()