import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler
import csv
import random
quotesArr = []

# Authenticate to Twitter
auth = tweepy.OAuthHandler("{key}", 
    "{key}")
auth.set_access_token("{key}", 
    "{key}")


# Create API object
api = tweepy.API(auth)


def tweet():
    api.update_status(random.choice(quotesArr))

#Logic for quotes

with open('D:/Projects/twitter bot/quotes.csv','r') as quotesFile:
    csvreader = csv.reader(quotesFile, delimiter = ",")
    line_count=0
    next(csvreader)
    for row in csvreader:
        if (int(row[2]) < 220):
            quotesArr.append('"' +row[0] + '"'+"-" + row[1])

tweet()
scheduler = BlockingScheduler()
scheduler.add_job(tweet, 'interval', minutes=45)
scheduler.print_jobs()
scheduler.start()

