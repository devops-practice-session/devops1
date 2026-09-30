#!/bin/bash
cd /home/ubuntu/hello-world-app
nohup gunicorn --bind 0.0.0.0:5000 app:app > app.log 2>&1 &
