""" pathlib--> find files 
    shutil --> move files
    os --> system operations"""
    
from pathlib import Path
import shutil

folder = Path("TestFolder")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Excel": [".xlsx", ".csv"]
}

# Create folders
for category in file_types:
    (folder/category).mkdir(exist_ok=True)

# Move files
for file in folder.iterdir():

    if file.is_file():

        for category, extensions in file_types.items():

            if file.suffix.lower() in extensions:

                destination = folder/category/file.name
                shutil.move(str(file), str(destination))
                print(f"Moved: {file.name} ➜ {category}")
                break

print("\nDone! Files organized successfully.")