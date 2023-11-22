import tkinter as tk
from tkinter import filedialog, PhotoImage
import vlc
import os

class VLCPlayer:
    def __init__(self, master, video_directory):
        self.master = master
        self.player = vlc.MediaPlayer()
        self.video_directory = video_directory
        self.video_files = self.get_video_files(video_directory)
        self.current_video_index = 0

        # Create open file button
        self.open_file_button = tk.Button(master, text="Open File", command=self.open_file)
        self.open_file_button.pack()

        # Create label to display video name
        self.video_name_label = tk.Label(master, text="")
        self.video_name_label.pack() 

        # Create play button
        self.play_button = tk.Button(master, text="Play", command=self.play_video)
        self.play_button.pack()

        # Create pause button
        self.pause_button = tk.Button(master, text="Pause", command=self.pause_video)
        self.pause_button.pack()

        # Create next button
        self.next_button = tk.Button(master, text="Next", command=self.play_next_video)
        self.next_button.pack()

        # Create skip intro buttons
        self.skip_button = tk.Button(master, text="Skip", command=lambda: self.skip_intro(5))
        self.skip_button.pack()

        # Create quit button
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_application)
        self.quit_button.pack()

    def get_video_files(self, directory):
        return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.mp4', '.avi', '.mkv'))]
    

    def open_file(self):
        # Open a dialog to choose a video file
        file_path = filedialog.askopenfilename(title="Select a video file", filetypes=(("Video files", "*.mp4 *.avi *.mkv"), ("All files", "*.*")))
        if file_path:
            media = vlc.Media(file_path)
            self.player.set_media(media)
            self.player.play()

    def play_video(self):
       if self.current_video_index < len(self.video_files):
        video_path = self.video_files[self.current_video_index]
        video_name = os.path.basename(video_path)
        self.video_name_label.config(text=video_name)  # Update the label with the video name
        media = vlc.Media(video_path)
        self.player.set_media(media)
        self.player.play()
        self.player.set_fullscreen(True)
        
        # Skip to 2 minutes and 20 seconds after the video starts
        self.player.set_time(140 * 1000)  # 140 seconds in milliseconds

    def pause_video(self):
        self.player.pause()

    def play_next_video(self):
        self.current_video_index += 1
        self.play_video()
    
    def skip_intro(self, minute):
        ms = minute * 60 * 1000
        self.player.set_time(ms)

    def quit_application(self):
        self.player.stop()  # Stop the VLC player
        self.master.destroy()  # Close the Tkinter window

# Create the main window
root = tk.Tk()

app = VLCPlayer(root, "C:\\Users\\lopes\\OneDrive\\One Pace\\ThrillerBark")
root.mainloop()
