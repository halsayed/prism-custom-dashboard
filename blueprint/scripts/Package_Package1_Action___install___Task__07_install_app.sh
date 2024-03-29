git clone https://github.com/halsayed/prism-custom-dashboard.git app

mkdir -p ./app/nginx/ssl
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
  -subj "/C=US/ST=NewYork/L=Springfield/O=Dis/CN=@@{address}@@" \
  -keyout ./app/nginx/ssl/nginx.key  -out ./app/nginx/ssl/nginx.cert
  
echo 'PRISM_HOST=@@{PRISM_HOST}@@
PRISM_PORT=@@{PRISM_PORT}@@' | tee ./app/.env
cd app
docker-compose up -d
