from customtkinter import *
from pytube import YouTube
from pathlib import Path

DOWNLOADS_FOLDER_PATH = Path.home() / "Downloads"


def download():
    try:
        yt_link = link.get()
        yt = YouTube(yt_link, on_progress_callback=on_progress)
        finished_label.configure(text="")
        yt.streams.get_highest_resolution().download(str(DOWNLOADS_FOLDER_PATH))
        finished_label.configure(text="Video downloaded! (look in the downloads folder)", text_color="green")
    except Exception as e:
        finished_label.configure(text=f"An error occurred: {e}", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    percentage.configure(text=per + '%')
    percentage.update()
    progressbar.set(float(percentage_of_completion) / 100)


# General system settings
set_appearance_mode("System")
set_default_color_theme("blue")

# App's frame
app = CTk()
app.geometry("360x240")
app.title("Youtube Downloader")
app.iconbitmap(".images/yt-downloader.ico")

# Title label
title = CTkLabel(app, text="Simple Youtube Downloader", font=("Outfit", 24))
title.pack(padx=10, pady=10)

# Entry field for the link
link = CTkEntry(app, placeholder_text="Paste here the link to a Youtube video...",
                width=260, height=40, bg_color='transparent')
link.pack()

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
