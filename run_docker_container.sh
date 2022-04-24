
timestamp=$(date +%Y%m%d%H%M%S)
container_name=demoapi_flask_ssqa_${timestamp}
echo ${container_name}
docker build -t demoapi_flask_ssqa .

docker run --name ${container_name} -d -p 8989:8989 demoapi_flask_ssqa
