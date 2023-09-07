#!/usr/bin/env bash

# su with a heredoc because this script is probably run as root
su steven <<EOSU
mkdir -p ~/tmp/endb/examples
cd ~/tmp/endb
rm -rf ~/tmp/endb/endb_data
cp -r ~/work/endatabas/endb/examples/endb* ~/tmp/endb/examples/.
EOSU
