from moviepy.editor import ImageSequenceClip, AudioFileClip
import os

# Set paths
image_folder = "resized_images"
audio_path = "output/audioScript.mp3"
output_path = "output/short.mp4"

# Function to sort image names numerically
def extract_number(filename):
    return int(os.path.splitext(filename)[0])  # "10.jpg" -> 10

# Load and sort image files numerically
images = sorted(
    [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith(".jpg")],
    key=lambda x: extract_number(os.path.basename(x))
)

print(f"Found {len(images)} images: {[os.path.basename(img) for img in images]}")

# Load audio
audioclip = AudioFileClip(audio_path)
audio_duration = audioclip.duration

# Adjust fps to match image count with audio duration
fps = len(images) / audio_duration

# Create video clip
clip = ImageSequenceClip(images, fps=fps).set_audio(audioclip.set_duration(audio_duration))

# Export video
clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
