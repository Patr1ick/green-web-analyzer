# Selenium Wire
from seleniumwire import webdriver
from selenium.webdriver import ChromeOptions
from seleniumwire.utils import decode

# Time
from datetime import datetime
import time
import pytz

# OS
import os

# Criterias
from .criteria import criteria_requests, criteria_img_types, criteria_img_compression

from .utils import create_folder, delete_folder


class Report:
    """Creates a report of a website"""

    def __init__(self, url) -> None:
        """
        Parameter
        ---
        url: string
        """
        self.url = url
        timezone = pytz.timezone("Europe/Berlin")
        self.date = datetime.now(timezone)
        # Initialize WebDriver
        self.options = ChromeOptions()
        self.options.headless = True
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')

        self.file_paths = {
            "html": [],
            "css": [],
            "js": [],
            "img": []
        }

        self.folder_name = f"request-{time.time()}"

        self.driver = webdriver.Chrome(options=self.options)
        self.driver.set_window_size(1920, 1080)

    def request_page(self) -> None:
        del self.driver.requests
        self.driver.start_session(self.options.to_capabilities())
        self.driver.get(self.url)

    def save_page(self) -> None:
        self.requests = list()

        self.full_size = 0

        for request in self.driver.requests:
            if request.response != None:
                response = {
                    "status_code": request.response.status_code if request.response.status_code else None,
                    "type": request.response.headers['Content-Type'],
                }
            else:
                response = None

            size = 0

            # Try to save it
            try:
                if (request.method == "GET" and
                    request.response != None and
                        request.response.status_code == 200):
                    body = decode(
                        request.response.body,
                        request.response.headers.get(
                            'Content-Encoding', 'identity')
                    )
                    path = request.path
                    if "text/html" in request.response.headers['Content-Type']:
                        # Root file (ex. "/")
                        if request.path[len(path)-1] == "/":
                            file_name = "/index.html"
                        # Sub-Domain file (ex. /de )
                        elif ".html" not in path:
                            file_name = path + ".html"
                        # Default
                    else:
                        file_name = path

                    file_path = f"./{self.folder_name}{file_name}"
                    folder_path = f"./{self.folder_name}{os.path.dirname(file_name)}"

                    # Add to file_paths
                    if "text/html" in request.response.headers['Content-Type']:
                        file_type = "html"
                    elif "text/css" in request.response.headers['Content-Type']:
                        file_type = "css"
                    elif "application/javascript" in request.response.headers['Content-Type']:
                        file_type = "js"
                    elif request.response.headers['Content-Type'] in ["image/gif", "image/jpeg", "image/png", "image/svg+xml", "image/webp"]:
                        file_type = "img"
                    self.file_paths[file_type].append({
                        "url": request.url,
                        "path": file_path,
                        "type": request.response.headers['Content-Type']
                    })
                    # Write to file
                    os.makedirs(
                        folder_path,
                        exist_ok=True
                    )

                    with open(file_path, "wb") as f:
                        f.write(body)

                    size = os.path.getsize(file_path)

            except NotADirectoryError as err:
                # TODO Replace with logging
                # TODO Create better error messages for debugging
                print("Error", err)
            finally:
                r = {
                    "url": request.url,
                    "path": request.path,
                    "method": request.method,
                    "response": response,
                    "date": request.date,
                    "size": size
                }
                self.requests.append(r)
                self.full_size += size

    def get_amount_requests(self) -> int:
        return len(self.requests)

    def create_report(self) -> dict:
        # Start
        create_folder(self.folder_name)

        # Request the page with Selenium Wire
        self.request_page()

        # Request page with Selenium Wire
        self.save_page()

        # Criteria 0: Outgoing Request
        criteria_0 = criteria_requests(self.requests)

        # Criteria 1: Images Types
        criteria_1 = criteria_img_types(self.file_paths['img'])

        # Criteria 2: Image Compression
        criteria_2 = criteria_img_compression(self.file_paths['img'])

        # Combine
        criterias = [
            criteria_0,
            criteria_1,
            criteria_2
        ]

        # End
        delete_folder(self.folder_name)

        # Generate Metrics
        # size = get_folder_size(self.folder_name)
        # Get amount of all requests made
        amount_requests = self.get_amount_requests()

        metrics = {
            "size": self.full_size,
            "requests": amount_requests,
            "potential_savings": criteria_1['details']['size_actual'] - criteria_1['details']['size_webp']
        }

        # Create report
        self.report = {
            "url": self.url,
            "date": self.date,
            "metrics": metrics,
            "criteria": criterias,
        }
        return self.report
