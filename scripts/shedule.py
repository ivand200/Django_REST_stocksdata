import os
from apscheduler.schedulers.blocking import BlockingScheduler


#os.system("python manage.py bot")
def div():
    os.system("python manage.py runscript div")

def dj30():
    os.system("python manage.py runscript dj30")

def sp500():
    os.system("python manage.py runscript sp500")

def index():
    os.system("python manage.py runscript index")
"""
scheduler = BlockingScheduler()
scheduler.add_job(div, 'interval', days=30, start_date="2020-05-01", end_date="2024-12-30")
scheduler.add_job(dj30, 'interval', days=25, start_date="2020-05-02", end_date="2024-12-30")
scheduler.add_job(sp500, 'interval', days=26, start_date="2020-05-03", end_date="2024-12-30")
scheduler.add_job(index, 'interval', days=27, start_date="2020-05-04", end_date="2024-12-30")
scheduler.start()"""
