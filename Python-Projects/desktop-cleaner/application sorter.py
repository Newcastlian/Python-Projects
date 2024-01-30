import os
import shutil
from pathlib import Path

def organize_applications():
    desktop_path = Path(os.path.expanduser("~/Desktop"))
    applications_folder_path = desktop_path / "Applications"

    # Create a folder named Applications if it doesn't exist
    applications_folder_path.mkdir(exist_ok=True)

    # Get a list of executable files on the desktop
    applications = [f for f in desktop_path.iterdir() if f.is_file() and f.suffix.lower() == ".exe" or f.suffix.lower() == ".lnk" or f.suffix.lower() == ".url"]

    # Move each application to the Applications folder
    for app in applications:
        destination = applications_folder_path / app.name
        shutil.move(str(app), str(destination))
        print(f"Moved {app.name} to {destination}")

if __name__ == "__main__":
    organize_applications()
