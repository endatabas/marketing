#!/usr/bin/env bash

# demo-magic via https://github.com/paxtonhare/demo-magic
#            via https://jromers.github.io/article/2019/10/running-cli-demo/
# pv via `sudo apt-get install pv`
#    via `brew install pv`

. demo-magic.sh
mkdir -p ~/tmp/endb
cd ~/tmp/endb
rm -rf ~/tmp/endb/endb_data

# UNIXPROMPT="$ "
# function prompt
# {
#     echo; echo "------> $*"
# }
function space
{
    echo;
}
clear

pei "pwd"
pei "ls -l"
pei "mkdir -p endb_data"
space
pei "docker pull docker.io/endatabas/endb"
space
pei "docker run --rm -p 3803:3803 -v endb_data:/app/endb_data docker.io/endatabas/endb"

#pei "cd ~/work/endatabas/endb"
#pei "
