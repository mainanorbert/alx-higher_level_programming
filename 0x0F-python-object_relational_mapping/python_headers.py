#!/usr/bin/bash

# Install Python development headers and build essentials
sudo apt-get install python3-dev build-essential

# Install MySQL development headers and client library
sudo apt-get install libmysqlclient-dev

# Install pkg-config
sudo apt-get install pkg-config

# Install zlib development headers (optional but often needed)
sudo apt-get install zlib1g-dev

# Install mysqlclient Python package
sudo pip3 install mysqlclient
