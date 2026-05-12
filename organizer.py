import os
import shutil

# Your folder path
path = input("Enter folder path: ").strip()

# Folders to create
folders = ["Images", "Documents", "Videos"]

# Step 1: Create folders if not exist
for folder in folders:
    folder_path = os.path.join(path, folder)
    
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Created folder: {folder}")

# Step 2: Move files
for file in os.listdir(path):
    full_path = os.path.join(path, file)

    if os.path.isfile(full_path):
        name, ext = os.path.splitext(file)
        ext = ext.lower()   # important for .JPG, .PDF etc.

        if ext in [".jpg", ".png", ".jpeg"]:
            shutil.move(full_path, os.path.join(path, "Images", file))
            print(f"Moved {file} → Images")

        elif ext in [".pdf", ".txt", ".docx"]:
            shutil.move(full_path, os.path.join(path, "Documents", file))
            print(f"Moved {file} → Documents")

        elif ext in [".mp4", ".mkv", ".avi"]:
            shutil.move(full_path, os.path.join(path, "Videos", file))
            print(f"Moved {file} → Videos")