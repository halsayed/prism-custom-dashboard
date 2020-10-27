
echo '
[Unit]
Description=demo web application
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/centos/
Environment=PRISM_IP=10.38.11.9
Environment=PRISM_REDIRECT="https://10.38.11.44/console/"
ExecStart=/bin/python3 wsgi.py
Restart=always

[Install]
WantedBy=multi-user.target' | sudo tee /etc/systemd/system/custom-login.service
