from tkinter import *
from tkinter import filedialog
from moviepy.editor import *

# Define the function to choose the input audio file
def choose_audio():
    global audio_path
    audio_path = filedialog.askopenfilename()

# Define the function to choose the input image file
def choose_image():
    global image_path
    image_path = filedialog.askopenfilename()

# Define the function to combine the audio and image files into an MP4 video
def combine_files():
    # Load the input audio and image files
    audio_file = AudioFileClip(audio_path)
    image_file = ImageClip(image_path)

    # Set the duration of the output video to be the same as the audio file
    duration = audio_file.duration

    # Set the output video's dimensions to match the input image file's dimensions
    dimensions = image_file.size

    # Create a VideoClip with the image and set its duration to match the audio file
    video_clip = ImageClip(image_path, duration=duration)

    # Add the audio to the VideoClip
    final_clip = video_clip.set_audio(audio_file)

    # Set the final clip's dimensions and write it to an MP4 file
    final_clip = final_clip.resize(dimensions)
    final_clip.write_videofile('output.mp4', fps=24)

# Create the GUI
root = Tk()

# Set the window title
root.title("Combine MP3 and Image into MP4")

# Create the "Choose Audio" button
audio_button = Button(root, text="Choose Audio", command=choose_audio)
audio_button.pack()

# Create the "Choose Image" button
image_button = Button(root, text="Choose Image", command=choose_image)
image_button.pack()

# Create the "Combine Files" button
combine_button = Button(root, text="Combine Files", command=combine_files)
combine_button.pack()

# Start the main loop
root.mainloop()
