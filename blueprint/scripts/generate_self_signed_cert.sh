#!/bin/bash
set -ex

sudo mkdir -p /etc/ssl/private
sudo openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
    -subj "/C=US/ST=NewYork/L=Springfield/O=Dis/CN=@@{address}@@" \
    -keyout /etc/ssl/private/nginx.key  -out /etc/ssl/certs/nginx.cert