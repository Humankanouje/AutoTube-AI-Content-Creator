## 1. pehele virtual env banana

## 2. phir .\venv\Scripts\activate

## 3. phir requirements.txt ko usme download karna

# every time you start terminal

.\venv\Scripts\activate

run launcher.py



#
#
# GUIDE BY GITHUB AND ME....................................................................
#
#




# 🎬 AutoTube AI — YouTube Shorts Content Creator

Welcome to **AutoTube AI** — your personal AI-powered pipeline that auto-generates engaging YouTube Shorts using AI scripting, text-to-speech, image generation, and video compilation. One click and boom 💥 — your short is ready!

---

## 🔧 Features

- ✨ Auto-generates video scripts using **LLMs**
- 🗣 Converts script to speech using **gTTS**
- 🖼 Generates images using **DuckDuckGo Search**
- 🖌 Fixes any broken/corrupt images automatically
- 🎞 Combines everything into a complete **YouTube Short**
- 📁 Organized outputs (audio, images, final video)

---

## 📂 Project Structure

AutoTube AI Youtube Content Creator/ │ ├── scriptGenerator.py # Generates video script using AI ├── tts.py # Converts script to audio (mp3) ├── image-generator.py # Downloads relevant images ├── img_resizer.py # Fixes broken/corrupt image files ├── video-generator.py # Merges images + audio into a video ├── launcher.py # Runs the entire pipeline step-by-step ├── requirements.txt # All Python dependencies └── README.md # This file 🙂

yaml
Copy code

---

## 🚀 Quick Start

### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/autotube-ai.git
cd "AutoTube AI Youtube Content Creator"
2. Create & activate virtual environment:
bash
Copy code
python -m venv venv
.\venv\Scripts\activate
3. Install all dependencies:
bash
Copy code
pip install -r requirements.txt
4. Run the full pipeline:
bash
Copy code
python launcher.py
🧠 Tech Stack
Python 3.10+

gTTS for speech

moviepy for video editing

duckduckgo-search for images

Pillow for image handling

subprocess for automation

Optional: Langchain + Ollama for advanced LLM-based scripts

🤖 Notes
Make sure audioScript.mp3 is available if skipping TTS

Ensure all images are valid (handled by img_resizer.py)

Customize fps, durations, and script prompts as per your need

💡 TODO (optional)
 Add background music

 Add subtitles using moviepy or ffmpeg

 Export video directly to YouTube using API

 Add web UI using Streamlit or Gradio

🫶 Contribution
Feel free to fork, star ⭐, or submit PRs.
You can also DM me cool short videos made using this 😄

📜 License
MIT — Do anything, just give some credits if this helped you 🙌