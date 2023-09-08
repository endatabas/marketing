#!/usr/bin/env bash

set -e
set -x

curl -d "SELECT 'Hello World';" -H "Content-Type: application/sql" -X POST http://localhost:3803/sql

curl -d "INSERT INTO users (name) VALUES ('Tianyu')" -H "Content-Type: application/sql" -X POST http://localhost:3803/sql

cd ~/work/endatabas/endb/examples/

./endb_console.py
