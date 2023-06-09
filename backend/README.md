# Backend - Green-Web-Analyzer

The backend is written in Python with the webframework Flask. It provides a REST-API with a endpoint to request a report for a website. It utilies Selenium(-Wire) to load the website and retrieve all needed information of the website.

# Run the backend

In order to run the backend you can build and start the docker container via the `docker-compose-local.yaml`-file in the root directory. In the file you have multiple options to set to the environment variable:

| Variable        | Options                  | Description                                                                                                                                          |
| --------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| APP_ENVIRONMENT | `prod`, `local`, `debug` | `prod`: production usage <br /> `local`: local usage, CORS Header is set to localhost<br /> `debug`: same as `local`, but Flask debugging is enabled |
| APP_VERSION     | 0.0.0                    | irrelevant for local setup                                                                                                                           |
