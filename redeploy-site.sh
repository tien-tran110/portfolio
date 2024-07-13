#!/bin/bash

# Navigate to project directory
cd portfolio

# Fetch and reset git repository
git fetch && git reset origin/main --hard

# Activate the virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

systemctl start myportfolio
systemctl enable myportfolio

# If there are any changes to the service unit file 
systemctl daemon-reload
systemctl restart myportfolio

# Check for the status of the service
systemctl status myportfolio

