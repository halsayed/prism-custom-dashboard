#!/bin/bash

sudo yum install -y git
sudo yum install -y python3 python3-dev python3-pip
git clone https://github.com/halsayed/prism-custom-dashboard.git app
cd app/login
sudo -H pip3 install -r requirements.txt

echo '
[Unit]
Description=demo web application
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/centos/app/login
Environment=PRISM_IP=10.38.11.9
Environment=PRISM_REDIRECT="https://10.38.11.44/console/"
ExecStart=/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target' | sudo tee /etc/systemd/system/custom-login.service

sudo systemctl daemon-reload
