#6. Write a script that schedules multiple tasks: one to print "Lunch Time!" at 1 PM, and another to print "Wrap up work" at 6 PM.

import schedule
import time

def lunch():
    print("Lunch Time!")

def wrap():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(lunch)
    schedule.every().day.at("18:00").do(wrap)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
