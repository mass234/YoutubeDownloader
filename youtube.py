#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import tkinter
from tkinter import *
from pytube import YouTube
import webbrowser



def jump_to_link(url):
    webbrowser.open_new(url)

window = Tk()

window.geometry("500x300")

window.resizable(0,0)

window.title("Video Downloader App")

Label(window, text = "YouTube Video Downloader", font = ("Butler", 20, "bold")).pack()

link = StringVar()

Label(window, text = "URLはこちらに", font = ("Butler", 20, "bold")).place(x=140, y=50)
# Label(window, text = "By Mass(@ffids6)", font = ("Butler", 20, "bold")).place(x=140, y=240)

canvas = tkinter.Canvas(width=510, height=200, background="#eee")
canvas.place(x=20, y=140)

text = tkinter.Label(canvas, text="By Mass(@ffids6)", font = ("Bulter", 20, "bold") , foreground = "#\
499", cursor="star")
text.place(x=130, y=90, anchor=tkinter.NW)

text.bind("<Button-1>", lambda e:jump_to_link("https://twitter.com/ffids6"))

link_entered = Entry(window, width=70, textvariable = link).place(x=32, y=100)

def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text="動画がフォルダに保存されました！", font=("Butler", 15)).place(x=20, y=210)

Button(window, text="ダウンロード", font="Butler 15 bold", bg="alice blue", padx=2, command = downloader).place(x=180, y=150)
          

window.mainloop()


# In[ ]:




