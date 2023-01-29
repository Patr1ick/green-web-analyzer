from pathlib import Path

import os
import shutil


def get_folder_size(folder_name) -> int:
    """Returns the size of the folder where the webpage is saved."""
    root_directory = Path(f"./{folder_name}")
    return sum(
        f.stat().st_size for f in root_directory.glob('**/*') if f.is_file()
    )


def create_folder(folder_name) -> None:
    # Create Folder for requests
    os.mkdir(f"./{folder_name}")


def delete_folder(folder_name) -> None:
    shutil.rmtree(f"./{folder_name}")
