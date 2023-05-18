import schedule
import time

def say_hello():
    print("Olá, tudo bem?")

times = ["12:00", "15:00", "20:27", "20:28", "20:30"]
jobs = [schedule.every().day.at(time) for time in times]
[job.do(say_hello) for job in jobs]

while True:
    schedule.run_pending()
    time.sleep(1)