import csv
import cs50
# Группа вводится
group = 203 
from datetime import datetime
startDatetime = datetime(2020, 9, 7, 0, 0)
db = cs50.SQL("sqlite:///students.db")
res = db.execute("SELECT `lastName`, `firstName`, `surname`, `timestamp`, `githubName`  FROM students WHERE `group`=?", group)
for row in res:
    lastName = row["lastName"]
    firstName = row["firstName"]
    surname = row["surname"]
    githubName = row["githubName"]
    timestamp = row["timestamp"]
    d = datetime.strptime(timestamp,'%Y/%m/%d %H:%M:%S %p GMT+7') 

    if startDatetime < d:
        print(lastName,", ", firstName," | ",  githubName, " | ", d.date())
res = db.execute("SELECT COUNT(firstName) as N FROM students WHERE `group`=?", group)[0]
print(res['N'])
