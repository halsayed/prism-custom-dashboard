#!/bin/bash

# shellcheck disable=SC2016
echo '
server {
    listen 80;
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name localhost;

    ssl_certificate /etc/ssl/certs/nginx.cert;
    ssl_certificate_key /etc/ssl/private/nginx.key;

    ssl_protocols TLSv1.2 TLSv1.1 TLSv1;

    access_log /var/log/nginx/reverse-access.log;
    error_log /var/log/nginx/reverse-error.log;

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
        proxy_pass http://localhost:5000/;
    }
}' | sudo tee /etc/nginx/conf.d/default.conf
sudo systemctl restart nginx