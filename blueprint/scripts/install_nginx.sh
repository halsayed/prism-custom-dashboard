#!/bin/bash
set -ex

# update and install nginx
sudo yum update -y
sudo yum -y install epel-release
sudo yum install -y nginx

# enable and start nginx
sudo systemctl start nginx
sudo systemctl enable nginx
