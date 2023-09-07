#!/usr/bin/env bash

# su with a heredoc because this script is probably run as root
su steven <<EOSU
mkdir -p ~/tmp/endb/examples
cd ~/tmp/endb
rm -rf ~/tmp/endb/demo_data
docker volume rm --force demo_data
cp -r ~/work/endatabas/endb/examples/endb* ~/tmp/endb/examples/.
mkdir -p ~/tmp/endb/demo_data
EOSU
