import schedule
import time

def job():
    print("Call our telegram script.")

schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("15:56").do(job)

count = 0
while count<=3:
    schedule.run_pending()
    time.sleep(1)
    # Turn off system