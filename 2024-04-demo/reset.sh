#!/usr/bin/env bash

# su with a heredoc because this script is probably run as root
su steven <<EOSU
mkdir -p ~/tmp/endb/examples
cd ~/tmp/endb
docker volume rm --force demo_data || echo "No demo_data Docker volume found. Ignoring."
rm -rf ~/tmp/endb/demo_data
mkdir -p ~/tmp/endb/demo_data
EOSU
