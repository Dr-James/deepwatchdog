from polls.models import Picture
import os
import glob
import datetime


def create_pictures():
    os.chdir('/Users/DJames9238/PycharmProjects/deepwatchdog/media/')
    counter = 0
    for file in glob.glob("*.png"):
        picture = Picture(counter, 1, datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S'), "/media/" + file)
        picture.save()
        counter += 1
    os.chdir('/Users/DJames9238/PycharmProjects/deepwatchdog/')