#!/usr/bin/env bash

# demo-magic via https://github.com/paxtonhare/demo-magic
#            via https://jromers.github.io/article/2019/10/running-cli-demo/
# pv via `sudo apt-get install pv`
#    via `brew install pv`

. demo-magic.sh -d -w5

function space
{
    echo;
}
clear

pei "curl -d \"SELECT 'Hello World';\" -H \"Content-Type: application/sql\" -X POST http://localhost:3803/sql"

pei "curl -d \"INSERT INTO users (name) VALUES ('Tianyu')\" -H \"Content-Type: application/sql\" -X POST http://localhost:3803/sql"

#pei 'curl -d "SELECT * FROM users" -H "Content-Type: application/sql" -X POST http://localhost:3803/sql'

pei "cd ~/work/endatabas/endb/examples/"

pei "./endb_console.py"

#pei "SELECT * FROM users;"
