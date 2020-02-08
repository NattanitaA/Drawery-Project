import csv
import datetime
import schedule
import time


def timetracker():

    lst = []
    myFile = open('drawery.csv', 'r')
    with myFile:
        csv_reader = csv.reader(myFile,delimiter= ',')
        line_count = 0
        next(csv_reader)
        for row in csv_reader:
            tempdate = datetime.datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f')
            difdate = datetime.datetime.now() - tempdate
            if difdate.days < 7:
                lst.append(row)
    myFile.close()

    myFile = open('drawery.csv', 'w')
    with myFile:
        lst = [['ID','user_name','status','open_time','close_time']] + lst
        writer = csv.writer(myFile)
        # for item in lst:
        writer.writerows(lst)
    myFile.close()

schedule.every().day.at("00:00").do(timetracker)

while 1:
    schedule.run_pending()
    time.sleep(1)





