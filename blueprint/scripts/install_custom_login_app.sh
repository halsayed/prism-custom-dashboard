#!/bin/bash

# clone custom login repo
sudo git clone https://github.com/halsayed/prism-custom-dashboard.git /app

# generate self-signed certificate for nginx
sudo mkdir -p /app/nginx/ssl
sudo openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
    -subj "/C=US/ST=NewYork/L=Springfield/O=Dis/CN=@@{address}@@" \
    -keyout /app/nginx/ssl/nginx.key  -out /app/nginx/ssl/nginx.crt

# update nginx default config
echo 'server {
    listen 80;
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name localhost;

    ssl_certificate /etc/nginx/ssl/nginx.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx.key;

    ssl_protocols TLSv1.2 TLSv1.1 TLSv1;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    location ~ ^/$ {
        if ($http_cookie !~* "NTNX_IGW_SESSION") {
            return 301 https://$host/login/;
        }
        proxy_pass https://@@{PRISM_IP}@@:@@{PRISM_PORT}@@;
    }

    location / {
        proxy_pass https://@@{PRISM_IP}@@:@@{PRISM_PORT}@@;
    }

    location /login/ {
        proxy_pass http://login:5000/;
    }
}' | sudo tee /app/nginx/conf.d/default.conf


# update docker-compose file
echo 'version: "3.0"
services:
  nginx:
    build: ./nginx/.
    restart: always
    ports:
      - "443:443"
  login:
    build: ./login/.
    restart: always
    environment:
      - PRISM_IP=@@{PRISM_IP}@@
      - PRISM_PORT=@@{PRISM_PORT}@@
      - PRISM_REDIRECT=https://@@{address}@@/console/' | sudo tee /app/docker-compose.yml

# start docker compose
cd /app
sudo sudo /usr/local/bin/docker-compose up -d

