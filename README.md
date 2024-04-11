## Getting Started
Dependencies:
* .env - should contain the OPEN_WEATHER_APP_ID for https://openweathermap.org/api 
* Docker - See [Get Docker](https://docs.docker.com/get-docker/)
* Docker Compose - Installed with Docker Desktop, See [Install Docker Compose](https://docs.docker.com/compose/install/)

With the dependencies installed, running the project is as simple as running:
```bash
docker compose up
```

This will pull the required Docker images and spin up a container running the service on http://127.0.0.1:5050.

To end the service, press `Ctrl+C`

## GET /run-advice?city=manila
This endpoint returns air pollution data for Manila to help determine if it is a good day to run outdoors. 

### Usage
```
curl 'http://127.0.0.1:5050/run-advice?city=manila'
```

### Status 200 Response
```commandline
{
  "data": {
    "co": 988.01,
    "nh3": 20.52,
    "no": 2.32,
    "no2": 36.67,
    "o3": 0.53,
    "pm10": 44.42,
    "pm2_5": 23.98,
    "so2": 19.55
  },
  "message": "Air quality is Fair right now",
  "status": "ok"
}
```

### Status 401 Response
```commandline
{
  "message": "City=tokyo is not supported",
  "status": "failed"
}
```