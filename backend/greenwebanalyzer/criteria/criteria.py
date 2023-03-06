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
        "id": 3,
        "accepted": len(compressed_images) == 0,
        "details": {
            "img": compressed_images
        }
    }


def criteria_minified_files(file_paths, app) -> dict:
    minified_files = {
        'js': [],
        'css': []
    }
    actual_size_js = 0
    potential_savings_js = 0
    # JavaScript files
    for js in file_paths['js']:
        output = f"{js['path']}.min.js"

        minify.file(js['type'].split(';')[0], js['path'], output)

        actual_size = os.path.getsize(js['path'])
        actual_size_js += actual_size
        output_size = os.path.getsize(output)
        potential_savings = actual_size - output_size
        potential_savings_js += potential_savings
        minified_files['js'].append({
            "url": js['url'],
            "actual_size": actual_size,
            "minified_size": output_size
        })

    actual_size_css = 0
    potential_savings_css = 0
    for css in file_paths['css']:
        output = f"{css['path']}.min.css"
        minify.file('text/css', css['path'], output)
        actual_size = os.path.getsize(css['path'])
        actual_size_css += actual_size
        output_size = os.path.getsize(output)
        potential_savings = actual_size - output_size
        potential_savings_css += potential_savings

        minified_files['css'].append({
            "url": css['url'],
            "actual_size": actual_size,
            "minified_size": output_size
        })

    return {
        "id": 4,
        "accepted": True,
        "details": {
            "files": minified_files,
            "actual_size_js": actual_size_js,
            "actual_size_css": actual_size_css,
            "potential_savings_js": potential_savings_js,
            "potential_savings_css": potential_savings_css
        }
    }
