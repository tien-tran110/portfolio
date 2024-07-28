#!/bin/bash

# Navigate to project directory
cd portfolio

# Fetch and reset git repository
git fetch && git reset origin/main --hard

# Spin containers down to prevent out of memory issues on our VPS
docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build

