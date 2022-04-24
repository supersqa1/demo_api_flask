
timestamp=$(date +%Y%m%d%H%M%S)
container_name=demoapi_flask_ssqa_${timestamp}
echo ${container_name}
docker build --no-cache -t demoapi_flask_ssqa .

docker run --name ${container_name} -d -p 5001:5001 demoapi_flask_ssqa
