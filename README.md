# PixelPlace

A simple collaborative pixel canvas built with **Python** and **Flask**, ready to deploy with **Docker Compose**.

It runs in localhost:5000 which is customizable. 

## Features

- Flask-based backend
- 64x64 pixel canvas (customizable)
- Easy deployment with Docker
- The canvas is currently stored in RAM, meaning all drawings are lost when the app is restarted

## Getting Started

### Running Locally
Run it directly from pixelplace.py. You'll need to install the required dependencies:
```
pip install Flask flask-socketio eventlet
```
and then
```
python pixelplace.py
```

### Docker Run
Run it from docker
```bash
docker-compose up --build

```



https://github.com/user-attachments/assets/112662a2-b1c0-45e3-8196-b8d6b0487cf0

