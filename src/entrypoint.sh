#!/usr/bin/env bash

echo "Wait MongoDB...";
python3 "src/utils/wait_mongo_db.py";

echo "Run mi-trainee-task service...";
gunicorn src.main.app -w 4 -b :$PORT -k uvicorn.workers.UvicornWorker;
