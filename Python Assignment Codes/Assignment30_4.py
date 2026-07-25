import time,schedule

def Display():
    print("Namaskar...")

def main():
    schedule.every().day.at("09:00").do(Display)

    while  True:
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__": 
    main()