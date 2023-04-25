from tkinter import *
from tkinter import filedialog
from moviepy.editor import *

def choose_audio():
    global audio_path
    audio_path = filedialog.askopenfilename()

def choose_image():
    global image_path
    image_path = filedialog.askopenfilename()

def combine_files():
    # Load the input audio and image files
    audio_file = AudioFileClip(audio_path)
    image_file = ImageClip(image_path)

    duration = audio_file.duration

    dimensions = image_file.size

    video_clip = ImageClip(image_path, duration=duration)
    final_clip = video_clip.set_audio(audio_file)
    final_clip = final_clip.resize(dimensions)
    final_clip.write_videofile('output.mp4', fps=24)

root = Tk()
root.title("Combine MP3 and Image into MP4")
audio_button = Button(root, text="Choose Audio", command=choose_audio)
audio_button.pack()
image_button = Button(root, text="Choose Image", command=choose_image)
image_button.pack()
combine_button = Button(root, text="Combine Files", command=combine_files)
combine_button.pack()

root.mainloop()
