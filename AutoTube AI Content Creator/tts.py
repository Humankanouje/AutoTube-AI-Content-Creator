import os
import time
from gtts import gTTS

# Path to the input script
script_path = os.path.join("output", "script.txt")

# Check if script.txt exists
if not os.path.exists(script_path):
    print("❌ script.txt not found in output folder.")
    exit()

# Read script content
with open(script_path, "r", encoding="utf-8") as m:
    script_text = m.read().strip()

if not script_text:
    print("❌ script.txt is empty.")
    exit()

# Adjust script for natural tone (conversational, energetic)
# Add some pauses and emphasize certain parts by using punctuation (like exclamation marks)
modified_script = script_text.replace("!","! ")
modified_script = modified_script.replace(".", ". ")

# Add pauses (inserting '...') for dramatic effect, wherever needed
modified_script = modified_script.replace("like", "like...")  # Adding a pause after "like"

# Convert the adjusted script to speech
tts = gTTS(text=modified_script, lang='en')

# Save audio
audio_path = os.path.join("output", "audioScript.mp3")
tts.save(audio_path)

print(f"✅ Audio file saved as: {audio_path}")
