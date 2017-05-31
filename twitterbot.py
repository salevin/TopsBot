import tweepy
import datetime
from time import sleep
from credentials import *
from random import shuffle

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

video = ("https://www.youtube.com/embed/videoseries?"
         "list=PLNiBGVBxUyyAFeryQR1Dhykhoi836K_eI&index=")

tweet = "Tops song of the day 💓: "


def vidGen():
    songs = []
    while True:
        if not songs:
            songs = [str(i) for i in range(15)]
            shuffle(songs)
        yield songs.pop()


if __name__ == "__main__":
    t = datetime.datetime.today() + datetime.timedelta(days=1)
    s = t.replace(hour=5, minute=30, second=0) - datetime.datetime.now()
    print(s)
    sleep(s.seconds)
    while False:
        for song in vidGen():
            cur = video + song
            print(cur)
            api.update_status(tweet + cur)
            sleep(24*60*60)
