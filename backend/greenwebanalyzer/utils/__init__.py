from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

import os
import shutil
import json


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


def checkEnergy(url) -> dict:
    result = {
        "green": False,
        "hosted_by": "",
        "details": None
    }
    hostname = urlparse(url).hostname

    with urlopen(
        f"https://api.thegreenwebfoundation.org/api/v3/greencheck/{hostname}"
    ) as f:
        response = json.load(f)

    if response['green']:
        result["green"] = True
        result["hosted_by"] = response['hosted_by']
        result["details"] = response['supporting_documents']

    return result
