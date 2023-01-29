import os

# Image Proccessing
from PIL import Image


def criteria_requests(requests) -> dict:
    return {
        "id": 0,
        "accepted": True,
        "details": {
            "requests": requests,
        }
    }


def criteria_img_types(img_file_paths) -> dict:
    bad_images = []
    size_actual, size_webp = 0, 0
    for img in img_file_paths:
        if img['type'] == "image/jpeg" or img['type'] == "image/png" or img['type'] == "image/gif":

            # Convert to webp
            webp_path = f"{img['path']}.webp"

            image = Image.open(img['path'])
            image.save(webp_path, format="webp")

            img_size = os.path.getsize(img['path'])
            img_webp_size = os.path.getsize(webp_path)

            bad_images.append({
                "url": img['url'],
                "type": img['type'],
                "actual_size": img_size,
                "webp_size": img_webp_size
            })

            size_actual += img_size
            size_webp += img_webp_size

            os.remove(webp_path)

    return {
        "id": 1,
        "accepted": len(bad_images) == 0,
        "details": {
            "img": bad_images,
            "size_actual": size_actual,
            "size_webp": size_webp
        }
    }


def criteria_img_compression(img_file_paths) -> dict:
    compressed_images = []
    for img in img_file_paths:
        if img['type'] == "image/jpeg":
            actual_size = os.path.getsize(img['path'])

            im = Image.open(img['path'])
            im.save(img['path'] + 'buffer.jpeg', "JPEG", quality=50)

            compressed_size = os.path.getsize(img['path'] + 'buffer.jpeg')

            if compressed_size < actual_size:
                compressed_images.append({
                    "url": img['url'],
                    "type": img['type'],
                    "actual_size": actual_size,
                    "compressed_size": compressed_size
                })

            os.remove(img['path'] + 'buffer.jpeg')

    return {
        "id": 2,
        "accepted": len(compressed_images) == 0,
        "details": {
            "img": compressed_images
        }
    }
