#4. Create a task that runs once every day at 9:00 AM and prints "Namskar..."

import time
import schedule

def Namaskar():
    print("Namskar...")

def main():
    schedule.every().day.at("09:00").do(Namaskar)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()