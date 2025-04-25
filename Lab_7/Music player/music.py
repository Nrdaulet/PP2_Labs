from tkinter import *
import pygame
from tkinter import filedialog
import os

root = Tk()
root.title("Nur")
root.geometry("500x300")

pygame.mixer.init()


def add_song():
    song = filedialog.askopenfilename(initialdir='Lab_7/Music player/audio', 
                                      title='Choose A Song',
                                      filetypes=(('mp3 Files', '*.mp3'),))
    song = os.path.basename(song)  # Получаем только имя файла
    song = song.replace('.mp3', '')  # Убираем расширение
    song_box.insert(END, song)


def play():
    song = song_box.get(ACTIVE)
    song = f'Lab_7/Music player/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

global paused
paused = False

def next():
    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    song = f'Lab_7/Music player/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #Move active bar in playlist listbox
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)

def previos_song():
    next_one = song_box.curselection()
    next_one = next_one[0]-1
    song = song_box.get(next_one)
    song = f'Lab_7/Music player/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #Move active bar in playlist listbox
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)



def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

    
    


song_box = Listbox(root, bg='black', fg="pink", width=60, selectbackground='blue')
song_box.pack(pady=20)


back_btn_img = PhotoImage(file='Lab_7/Music player/mcont/back.png')
forward_btn_img =PhotoImage(file='Lab_7/Music player/mcont/next.png')
play_btn_img =PhotoImage(file='Lab_7/Music player/mcont/play.png')
pause_btn_img =PhotoImage(file='Lab_7/Music player/mcont/pause.png')
stop_btn_img =PhotoImage(file='Lab_7/Music player/mcont/stop.png')

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame,image=back_btn_img, borderwidth=0, command=previos_song)
forward_button =Button(controls_frame,image=forward_btn_img, borderwidth=0, command=next)
play_button =Button(controls_frame,image=play_btn_img, borderwidth=0, command=play)
stop_button =Button(controls_frame,image=stop_btn_img, borderwidth=0, command=stop)
pause_button =Button(controls_frame,image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)
pause_button.grid(row=0, column=4, padx=10)

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add Songs
add_songs_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_songs_menu)
add_songs_menu.add_command(label="Add One Song to Playlist", command=add_song)

root.bind('<space>', lambda event: pause(paused))
root.mainloop()