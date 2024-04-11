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
    "co": 1121.52,
    "nh3": 14.57,
    "no": 14.19,
    "no2": 30.5,
    "o3": 19.13,
    "pm10": 53.41,
    "pm2_5": 30.8,
    "so2": 34.33
  },
  "message": "Air quality is Moderate right now; You could run!",
  "status": "ok"
}
```

### Status 400 Response
```commandline
{
  "message": "City=tokyo is not supported",
  "status": "failed"
}
```

### Status 401 Response
```commandline
{
  "data": {
    "cod": 401,
    "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."
  },
  "status": "failed",
  "url": "https://api.openweathermap.org/data/2.5/air_pollution?appid=<invalid-app-id>&lat=14.5995&lon=120.9842"
}
```