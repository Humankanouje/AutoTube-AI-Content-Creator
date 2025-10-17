# scriptGenerator.py

import os
import threading
import itertools
import time
import sys
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Spinner function
def spinner(msg, stop_event):
    spinner_cycle = itertools.cycle(['|', '/', '-', '\\'])
    while not stop_event.is_set():
        print(f'\r{msg} {next(spinner_cycle)}', end='', flush=True)
        time.sleep(0.1)
    print('\r' + ' ' * (len(msg) + 2), end='\r')  # Clear line

# Check for command-line argument
if len(sys.argv) < 2:
    print("❌ Please provide a topic as an argument.")
    print("Usage: python scriptGenerator.py 'what is blackhole'")
    sys.exit(1)

# Get topic from command-line arguments
topic = " ".join(sys.argv[1:])

# Detect language (basic keyword check)
def detect_language(text):
    hindi_keywords = ['क्या', 'कैसे', 'क्यों', 'है', 'से', 'तक', 'और', 'तो', 'नहीं', 'करना']
    return "hi" if any(word in text for word in hindi_keywords) else "en"

language = detect_language(topic)

# Prompt template
template = """Write a short YouTube Shorts script (max 60 seconds, minimum 30 seconds) on the topic: "{topic}".

- If the topic is asked in Hindi, then the entire script must be written **completely in Hindi**, using a natural, casual, friendly tone, as if a young guy is speaking to friends.
- Start with: "Namaskar doston!" — energetic but real, not overacted.
- Continue straight into the topic without over-formality.
- Share 2–3 interesting, cool, or surprising facts related to the topic — but make sure the tone sounds like a chill conversation, not a lecture.
- Use everyday expressions like "socho zara", "mazedaar baat yeh hai", "bhai suno", "pata hai kya?", etc. to make it sound like a real person talking.
- Don’t explain emotions (like *smiles*, *laughs*). Just focus on what he would actually say.
- End the script with a casual question like: "tumhara favourite konsa hai?", or "kya tumne yeh pehle suna tha?", or "tum kya soch rahe ho?"
- Finally, end with ONLY ONE CTA depending on the language:
    - In Hindi: "Agar yeh video aapko acchi lagi ho, to like, share aur subscribe karna na bhoolen."
    - OR In English: "Don’t forget to like and subscribe."
- Do NOT mix both CTAs.
- Output only the natural script text — no labels, no formatting instructions, no headings. Just plain human-sounding speech content.
"""

# Create prompt
prompt = PromptTemplate(input_variables=["topic"], template=template)

# Load local model
llm = OllamaLLM(model="gemma3")

# Spinner while generating
stop_event = threading.Event()
spinner_thread = threading.Thread(target=spinner, args=("💡 Generating script with Gemma3...", stop_event))
spinner_thread.start()

# Generate script
final_prompt = prompt.format(topic=topic)
script = llm.invoke(final_prompt)

# Stop spinner
stop_event.set()
spinner_thread.join()

# Save script to file
os.makedirs("output", exist_ok=True)
with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("✅ Script generated and saved to output/script.txt")
