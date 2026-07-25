import time
import schedule

def WeeklyGoals():
    print("Start your weekly goals")

def WeeklyProgress():
    print("Review your weekly progress")

def WorkCompleted():
    print("Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(WeeklyGoals)
    schedule.every().wednesday.at("17:00").do(WeeklyProgress)
    schedule.every().friday.at("18:00").do(WorkCompleted)

    print("Weekly Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()