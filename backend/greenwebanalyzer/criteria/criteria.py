import os

# Image Proccessing
from PIL import Image

import minify


def criteria_requests(requests) -> dict:
    accepted = True

    for r in requests:
        if r['response'] == None:
            accepted = False

    return {
        "id": 0,
        "accepted": accepted,
        "details": {
            "requests": requests,
        }
    }


def criteria_redirects(requests) -> dict:
    amount = 0
    redirects = []
    for r in requests:
        if r['response'] != None:
            if r['response']['status_code'] == 301:
                amount += 1
                redirects.append(r)

    return {
        "id": 1,
        "accepted": amount < 1,
        "details": {
            "amount": amount,
            "redirects": redirects,
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
        "id": 2,
        "accepted": len(bad_images) == 0,
        "details": {
            "img": bad_images,
            "size_actual": size_actual,
            "size_webp": size_webp,
            "total_savings": size_actual - size_webp
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
        "id": 3,
        "accepted": len(compressed_images) == 0,
        "details": {
            "img": compressed_images
        }
    }


def criteria_minified_files(file_paths) -> dict:
    details = {
        'js': {
            'files': [],
            'total_size': 0,
            'total_minified_size': 0,
            'total_savings': 0

        },
        'css': {
            'files': [],
            'total_size': 0,
            'total_minified_size': 0,
            'total_savings': 0

        },
        'html': {
            'files': [],
            'total_size': 0,
            'total_minified_size': 0,
            'total_savings': 0

        },
        'total_savings': 0
    }

    for key in ['html', 'css', 'js']:
        for file in file_paths[key]:
            output_path = f"{file['path']}.min.{key}"

            minify.file(
                file['type'].split(';')[0],
                file['path'],
                output_path
            )

            minified_size = os.path.getsize(output_path)
            size = os.path.getsize(file['path'])
            potential_saving = size - minified_size

            # !TODO Add condition that not all savings are added
            # Add values
            details[key]['total_size'] += size
            details[key]['total_minified_size'] += minified_size
            details[key]['total_savings'] += potential_saving

            # Add file
            details[key]['files'].append({
                "url": file['url'],
                "size": size,
                "minified_size": minified_size
            })

        details['total_savings'] += details[key]['total_savings']

    return {
        "id": 4,
        "accepted": details['total_savings'] < 1000,
        "details": details
    }
