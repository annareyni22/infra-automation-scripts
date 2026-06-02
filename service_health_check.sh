#!/bin/bash

SERVICE=$1

systemctl is-active --quiet $SERVICE

if [ $? -eq 0 ]; then
    echo "$SERVICE is running"
else
    echo "$SERVICE is not running"
fi
