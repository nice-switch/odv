#!/bin/bash

if [ ! -d "venv" ]
then
    python3 -m venv venv
    
    ./venv/bin/python3 -m pip install --upgrade pip
    ./venv/bin/python3 -m pip install -r requirements.txt
fi

./venv/bin/python3 src/main.py

read -p "Press any key to continue..."