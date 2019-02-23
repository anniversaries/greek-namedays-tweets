# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import json
import datetime

# Loads namedays.json and gets today's anniversary
def getAnniversary():
    with open('namedays.json') as data_file:
        data = json.load(data_file)

        today = datetime.datetime.now()
        # %m is the two-digit representation of the current month
        # %d is the two-digit number of the current day
        monthAndDay = today.strftime("%d/%m")


    return data[monthAndDay] if data.get(monthAndDay) != None else "Τίποτα σπουδαίο σήμερα 😉"