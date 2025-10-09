"""
@TODO
Create a Python script that automatically organizes files in a folder (e.g., Downloads) into subfolders based on their file extensions (.jpg, .pdf, .txt, etc.).
Goal:
Practice using os Module
Bonus:
Add a logging system (log.txt) that records which files were organized.
"""
import os
import shutil

def organizer(folder_path):
    file_extensions = set()
    # Check if folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist")
        return

    if not os.listdir(folder_path):  # empty list means no files/subfolders
        print("Folder is empty")
        return
    for root, dirs, files in os.walk(folder_path):
        # Retrieve extensions and create folder based on their extension
        for f in files:
            if "." in f:
                split_files = f.split(".")
                file_extensions.add(split_files[-1])

    # Create directories with extension names and log actions
    with open("log.txt", "w") as log_file:
        for extension in file_extensions:
            # Check if folder with extension name already exists / If exists -> Delete -> Create
            if os.path.exists(os.path.join(folder_path, extension)):
                os.rmdir(os.path.join(folder_path, extension))
                print(f"Created folder {os.path.join(folder_path, extension)}")
                log_file.write(f"Folder:{extension} has created successfully.\n")
                os.mkdir(os.path.join(folder_path, extension))
            else:
                os.mkdir(os.path.join(folder_path, extension))
                print("Created folder " + os.path.join(folder_path, extension))
                log_file.write(f"Folder:{extension} has created successfully.\n")

        # Move files from root directory with extension to assigned folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                for extension in file_extensions:
                    if file.endswith(extension):
                        log_file.write(f"File:{extension} is moved to location: {os.path.join(folder_path, extension)}\n")
                        shutil.move(os.path.join(folder_path, file),os.path.join(folder_path, extension))
                        log_file.write(f"File:{extension} was moved successfully.\n")

if __name__ == '__main__':
    selected_directory = r"folder_path_with_files"
    organizer(selected_directory)