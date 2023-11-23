import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x600")
canvas.config(bg = 'black')

rootpath = "C:\\Users\Ash\Music" #The Location of the music folder 
extension = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file = "prev_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")
next_img = tk.PhotoImage(file = "next_img.png")

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text = prev_song_name)
    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

def pause():
    if pauseBtn["text"] == "Pause":
        mixer.music.pause()
        pauseBtn["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseBtn["text"] = "Pause"

listBox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100, font= ('poppins', 14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text='', bg = "black", fg = "yellow", width = 100, font= ('poppins', 14))
label.pack(padx = 15)

top = tk.Frame(canvas, bg = "Black")
top.pack(padx = 10, pady = 5, anchor = 'center')

prevBtn = tk.Button(canvas, text = "Prev", image = prev_img, bg = "Black", borderwidth = 0, command = prev)
prevBtn.pack(pady = 15, in_ = top, side = 'left') 

stopBtn = tk.Button(canvas, text = "Stop", image = stop_img, bg = "Black", borderwidth = 0, command = stop)
stopBtn.pack(pady = 15, in_ = top, side = 'left')

playBtn = tk.Button(canvas, text = "Play", image = play_img, bg = "Black", borderwidth = 0, command = select)
playBtn.pack(pady = 15, in_ = top, side = 'left')

pauseBtn = tk.Button(canvas, text = "Pause", image = pause_img, bg = "Black", borderwidth = 0, command = pause)
pauseBtn.pack(pady = 15, in_ = top, side = 'left')

nextBtn = tk.Button(canvas, text = "Next", image = next_img, bg = "Black", borderwidth = 0, command = next)
nextBtn.pack(pady = 15, in_ = top, side = 'left')



for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, extension):
        listBox.insert('end', filename)

canvas.mainloop()
