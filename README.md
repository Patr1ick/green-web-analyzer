# Green Web Analyzer

This is the source code of a student research project for the DHBW Stuttgart. It is a website which analyses a website in regard of data minimisation and efficiency.

## Local Setup

Node version: 18.13

### Backend

To start the backend you can use this with the docker-compose file and the following command:

```bash
docker compose -f docker-compose-local.yaml up -d
```

The backend will be exposed to the port 5000.

### Frontend

To start the frontend you need to be inside the `frontend` folder and run the development server:

```bash
cd frontend
npm run dev
```

## License

[BSD 3-Clause License](LICENSE.md)
