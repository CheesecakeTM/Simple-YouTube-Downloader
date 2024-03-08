from customtkinter import *
from pytube import YouTube
import os

DOWNLOADS_FOLDER_PATH = os.path.expanduser('~/Downloads')
DW_CHOICE = "Video"


def download():
    """ Download function."""

    yt_link = link.get()
    yt = YouTube(yt_link, on_progress_callback=on_progress)
    finished_label.configure(text="")
    if DW_CHOICE == "Video":
        try:
            yt.streams.get_highest_resolution().download(str(DOWNLOADS_FOLDER_PATH))
            finished_label.configure(text="Video downloaded! (look in the downloads folder)", text_color="green")
        except Exception as e:
            finished_label.configure(text=f"An error occurred: {e}", text_color="red")
    elif DW_CHOICE == "Audio":
        try:
            yt.streams.get_audio_only().download(str(DOWNLOADS_FOLDER_PATH))
            finished_label.configure(text="Audio downloaded! (look in the downloads folder)", text_color="green")
        except Exception as e:
            finished_label.configure(text=f"An error occurred: {e}", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    """ Progress bar and percentage update function."""

    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    percentage.configure(text=per + '%')
    percentage.update()
    progressbar.set(float(percentage_of_completion) / 100)


def combobox_callback(choice):
    """ Choice between video and audio."""

    global DW_CHOICE
    DW_CHOICE = choice


# General system settings
set_appearance_mode("System")
set_default_color_theme("blue")

# App's frame
app = CTk()
app.geometry("400x300")
app.title("Youtube Downloader")
app.iconbitmap("./dist/icon.ico")
app.maxsize(400, 300)
app.minsize(400, 300)


# Title label
title = CTkLabel(app, text="Simple Youtube Downloader", font=("Outfit", 24))
title.pack(padx=10, pady=10)

# Link field and drop-down menu frame:
frame = CTkFrame(app, width=320, height=50, bg_color='transparent')
frame.pack(pady=10, padx=10)

# - entry field for the link
link = CTkEntry(frame, placeholder_text="Paste here the link to a Youtube video...",
                width=250, height=40, bg_color='transparent')
link.pack(side=RIGHT, pady=10, padx=10)

# - drop-down menu to choose between mp3 and mp4
drop_down = CTkComboBox(frame, width=70, height=26, values=["Audio", "Video"], command=combobox_callback)
drop_down.pack(pady=20, padx=10)
drop_down.set("Video")

# Download button
button = CTkButton(app, text="Download", command=download)
button.pack(pady=10, padx=10)

# Finish label
finished_label = CTkLabel(app, text="", font=("Outfit", 15))
finished_label.pack(padx=10, pady=10)

# Download progress bar
percentage = CTkLabel(app, text="0%")
percentage.pack()

progressbar = CTkProgressBar(app, width=300)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

# Run app
app.mainloop()
