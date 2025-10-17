# imageDownloader.py

import os
import sys
import requests

UNSPLASH_ACCESS_KEY = "3dpqGt1dB5PZPvCcC_2VkkEYhjylIwGXu_lQupz32TI"

def download_unsplash_images(topic, limit=10):
    os.makedirs("images", exist_ok=True)
    print(f"\n🔍 Searching on Unsplash: {topic}\n")

    url = f"https://api.unsplash.com/search/photos?query={topic}&per_page={limit}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for i, photo in enumerate(data["results"]):
            img_url = photo["urls"]["regular"]
            img_path = os.path.join("images", f"{i+1}.jpg")

            try:
                img_data = requests.get(img_url).content
                with open(img_path, "wb") as f:
                    f.write(img_data)
                print(f"✅ Saved: {img_path}")
            except Exception as e:
                print(f"⚠️ Failed to download image {i+1}: {e}")
        print("\n🎉 All images downloaded successfully.")
    else:
        print("❌ Unsplash API Error:", response.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide a topic to search for images.")
        print("Usage: python imageDownloader.py blackhole")
        sys.exit(1)

    topic = " ".join(sys.argv[1:]).strip()
    download_unsplash_images(topic)
