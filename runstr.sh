set -a
source .env
set +a

docker stop py-js-instance
docker rm py-js-instance

docker build -t py-js .
docker run -d --name py-js-instance --env-file .env -p $PORT:$PORT py-js 