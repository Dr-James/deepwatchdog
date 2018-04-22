from polls.models import Picture
import os
import glob
import datetime


def create_pictures():
    os.chdir('/Users/DJames9238/PycharmProjects/deepwatchdog/media/')
    for file in glob.glob("*.png"):
        picture = Picture(Picture.objects.all().count(), 1, datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S'), "/media/" + file)
        picture.save()
    os.chdir('/Users/DJames9238/PycharmProjects/deepwatchdog/')