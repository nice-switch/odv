#!/bin/bash

if [ ! -d "venv/linux_env" ]
then
    python3 -m venv venv/linux_env
    
    ./venv/linux_env/bin/python3 -m pip install --upgrade pip
    ./venv/linux_env/bin/python3 -m pip install -r requirements.txt
fi

./venv/linux_env/bin/python3 src/main.py

read -p "Press any key to continue..."