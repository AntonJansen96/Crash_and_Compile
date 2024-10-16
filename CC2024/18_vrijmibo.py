#!/usr/bin/env python3

import sqlite3
import datetime


def isVrijmibo(date: str) -> bool:
    dateobj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    weekday = dateobj.weekday()
    hour = dateobj.hour
    return (weekday == 4 and hour >= 12) or (weekday == 5 and hour < 9)


# SQLite stuff
conn = sqlite3.connect("data/francken-transactions.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT * FROM transactions")

count = 0
for row in cursor:

    amount = int(row[0])
    date = row[1]
    category = row[-1]

    if category == "Beer" and isVrijmibo(date):
        count += amount

print(count)
