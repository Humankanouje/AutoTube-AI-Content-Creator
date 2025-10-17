# launcher.py

import subprocess
import sys

if len(sys.argv) < 2:
    print("❌ Please provide a topic.")
    print("Usage: python launcher.py 'blackhole'")
    sys.exit(1)

topic = " ".join(sys.argv[1:])  # In case topic has spaces

# 🧠 Script commands with topic injected directly
commands = [
    f"python scriptGenerator.py \"{topic}\"",  
    "python tts.py",                               
    f"python image-generator.py \"{topic}\"",      
    "python img_resizer.py",                        
    "python video-generator.py"                   
] 

print("\n🚀 Starting Full Short Video Generation Pipeline...\n")

for cmd in commands:
    print(f"\n▶️ Running: {cmd}")
    result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        print(f"❌ Error occurred while running: {cmd}")
        break
    else:
        print(f"✅ Completed: {cmd}\n" + "-" * 50)

print("\n🎉 Pipeline execution complete.")
