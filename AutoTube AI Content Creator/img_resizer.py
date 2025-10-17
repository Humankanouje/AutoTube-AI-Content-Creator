from PIL import Image
import os
import shutil

# Folder paths
input_folder = "images"
output_folder = "resized_images"
os.makedirs(output_folder, exist_ok=True)

# Base size
base_size = (1280, 720)

# Get sorted list of image files
image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))])

# To store last successful image path
last_good_image = None
count = 1

for filename in image_files:
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, f"{count}.jpg")  # Save with clean sequence names

    try:
        # Open and resize
        img = Image.open(input_path).convert("RGB").resize(base_size)
        img.save(output_path)
        last_good_image = output_path  # Update last good image
        print(f"✅ Saved: {output_path}")
    except Exception as e:
        print(f"⚠️ Error in {filename}, using previous image instead.")
        if last_good_image:
            shutil.copy(last_good_image, output_path)
            print(f"🌀 Duplicated from {last_good_image} -> {output_path}")
        else:
            print("❌ No previous good image to duplicate from. Skipping.")
            continue  # If first image is bad, skip
    count += 1
