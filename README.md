# Flsk app to demo REST API with Python & Docker

### To build the image
```
docker build -t <image name> .
```

### To run the application in docker
```commandline
docker run -p 5001:5001 <image name>
```

### To run the image that is published to DockerHub
```commandline
docker run -p 5001:5001 supersqa/demo_api_flask:latest
```