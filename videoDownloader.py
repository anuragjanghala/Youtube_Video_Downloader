from tkinter import *
from pytube import YouTube
from pytube import Playlist
import tkinter
import threading
import traceback


# FUNCTIONS


def download():

    global notif
    video_url = url.get()
    try:
        youtube = YouTube(video_url)
        video = youtube.streams.first()
        video.download("/home/anuragjanghala/Desktop")
        notif.config(fg="green", text="Download Complete")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="video could't be downloaded")


# MAIN SCREEN
master = Tk()
master.title("YOUTUBE VIDEO DOWNLOADER")

# LABELS
Label(master, text="YOUTUBE VIDEO CONVERTER", fg="black",
      font=("Calibri", 15)).grid(sticky=N, padx=100, pady=10, row=0)
Label(master, text="Please Enter the Link of the video below: ", fg="black",
      font=("Calibri", 15)).grid(sticky=N, padx=100, pady=15, row=1)
notif = Label(master, font=("Calibri", 13)).grid(
    sticky=N, pady=1, row=4)

# VARIABLES
url = StringVar()


# ENTRY
Entry(master, width=50, textvariable=url).grid(sticky=N, row=2)

# BUTTON
buttonp = Button(master, width=20, text="Download", font=(
    "Calibri", 10), command=download)
buttonp.grid(sticky=N, pady=15, row=3)
master.mainloop()
