import schedule
import time

def Display(Message):
    print(Message)

def main():
    Message = input("Enter Message : ")
    Interval = int(input("Enter interval in seconds : "))

    if Interval <= 0:
        print("Interval must be greater than zero")

    schedule.every(Interval).seconds.do(Display, Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()