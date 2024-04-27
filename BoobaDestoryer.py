import os

def delete_booba(root_folder):
    for folder_path, _, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Anime Booba be gone sigmas mindset or smth idk: {file_path}")
root_folder = input("Enter the songs folder path: ")

delete_booba(root_folder)
