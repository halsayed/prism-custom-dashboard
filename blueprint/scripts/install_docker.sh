#!/bin/bash
set -ex

# update and install nginx
sudo yum update -y
sudo yum -y install epel-release \
                    yum-utils \
                    git \
                    curl \
                    wget \
                    device-mapper-persistent-data \
                    lvm2

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker

sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# install docker-compose
curl -s https://api.github.com/repos/docker/compose/releases/latest \
  | grep browser_download_url \
  | grep docker-compose-Linux-x86_64 \
  | cut -d '"' -f 4 \
  | wget -qi -
chmod +x docker-compose-Linux-x86_64
sudo mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose