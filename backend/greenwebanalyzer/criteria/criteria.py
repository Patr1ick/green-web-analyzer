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
    details = {
        "amount": 0,
        "redirects": [],
    }
    for r in requests:
        if r['response'] != None:
            if r['response']['status_code'] == 301:
                details['amount'] += 1
                details['redirects'].append(r)

    return {
        "id": 1,
        "accepted": details['amount'] < 1,
        "details": details
    }


def criteria_img_types(img_file_paths) -> dict:
    details = {
        "files": [],
        "total_size": 0,
        "total_size_webp": 0,
        "total_savings": 0
    }

    for img in img_file_paths:
        if img['type'] in ["image/jpeg", "image/png", "image/gif"]:

            # Convert to webp
            webp_path = f"{img['path']}.webp"

            image = Image.open(img['path'])
            image.save(webp_path, format="webp")

            size = os.path.getsize(img['path'])
            size_webp = os.path.getsize(webp_path)
            potential_saving = size - size_webp

            details['total_size'] += size
            details['total_size_webp'] += size_webp
            details['total_savings'] += potential_saving

            details['files'].append({
                "url": img['url'],
                "type": img['type'],
                "size": size,
                "size_webp": size_webp,
                "potential_saving": potential_saving
            })

            os.remove(webp_path)

    return {
        "id": 2,
        "accepted": len(details['files']) == 0,
        "details": details
    }


def criteria_img_compression(img_file_paths) -> dict:
    details = {
        "files": [],
        "total_size": 0,
        "total_size_compressed": 0,
        "total_savings": 0
    }
    for img in img_file_paths:
        if img['type'] == "image/jpeg":

            im = Image.open(img['path'])
            im.save(img['path'] + 'buffer.jpeg', "JPEG", quality=50)

            size = os.path.getsize(img['path'])
            compressed_size = os.path.getsize(img['path'] + 'buffer.jpeg')
            potential_saving = size - compressed_size

            if potential_saving > 1000:
                details['total_size'] += size
                details['total_size_compressed'] += compressed_size
                details['total_savings'] += potential_saving
                details['files'].append({
                    "url": img['url'],
                    "type": img['type'],
                    "size": size,
                    "size_compressed": compressed_size,
                    "potential_saving": potential_saving
                })

            os.remove(img['path'] + 'buffer.jpeg')

    return {
        "id": 3,
        "accepted": len(details['files']) == 0,
        "details": details
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
                "minified_size": minified_size,
                "potential_saving": potential_saving
            })

        details['total_savings'] += details[key]['total_savings']

    return {
        "id": 4,
        "accepted": details['total_savings'] < 1000,
        "details": details
    }
