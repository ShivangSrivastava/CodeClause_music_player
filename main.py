import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

class Player:
    def __init__(self):
        self.root = Tk()
        self.root.title("Music Player")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.config(bg="black")
        self.root.bind("<Escape>", self.root.quit)
        self.root.bind("<F11>", self.root.attributes("-fullscreen", True))
        self.root.bind("<F12>", self.root.attributes("-fullscreen", False))
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)

    def open_folder(self):
        self.folder = filedialog.askdirectory()
        self.songs = os.listdir(self.folder)
        self.songs.sort()
        self.listbox = Listbox(self.root, bg="black", fg="white", selectbackground="white", selectforeground="black")
        self.listbox.pack(expand=True, fill=BOTH)
        for song in self.songs:
            self.listbox.insert(END, song)
        self.listbox.bind("<Double-Button-1>", self.play_song)
        self.listbox.bind("<Button-1>", self.play_song)
        self.listbox.bind("<ButtonRelease-1>", self.play_song)
        self.listbox.bind("<Button-3>", self.play_song)
    
    # method to play songs
    def play_song(self, event=None):
        song = self.listbox.get(self.listbox.curselection()[0])
        mixer.init()
        mixer.music.load(os.path.join(self.folder, song))
        mixer.music.play()
        self.listbox.selection_set(self.listbox.curselection()[0])

    
    def pause_song(self):
        mixer.music.pause()
        self.root.update()
        self.root.update_idletasks()
    def resume(self):
        mixer.music.unpause()
        self.root.update()
        self.root.update_idletasks()
        
    def quit(self):
        mixer.music.stop()
        self.root.destroy()
        self.root.quit()

    def buttons(self):
        self.play_button = Button(self.root, text="Restart", bg="white", fg="black", command=self.play_song)
        self.play_button.pack(side=LEFT)
        self.pause_button = Button(self.root, text="Pause", bg="white", fg="black", command=self.pause_song)
        self.pause_button.pack(side=LEFT)
        self.resume_button = Button(self.root, text="Resume", bg="white", fg="black", command=self.resume)
        self.resume_button.pack(side=LEFT)
        self.quit_button = Button(self.root, text="Quit", bg="white", fg="black", command=self.quit)
        self.quit_button.pack(side=LEFT)
    
    
    def run(self):

        self.open_folder()
        self.buttons()
        self.root.mainloop()

Player().run()