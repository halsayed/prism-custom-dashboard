#!/bin/bash
set -ex

sudo yum update --quiet -y
sudo yum --quiet -y install epel-release \
                            yum-utils \
                            git \
                            curl \
                            wget \
                            device-mapper-persistent-data \
                            lvm2

#Remove any Old docker version
sudo yum remove docker docker-common container-selinux docker-selinux docker-engine
