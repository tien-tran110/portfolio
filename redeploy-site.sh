#!/bin/bash

#Kill active flask session
tmux kill-session -t flask_session
# Navigate to project directory
cd portfolio

# Fetch and reset git repository
git fetch && git reset origin/main --hard

# Activate the virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Create a script to start the Flask server
echo '#!/bin/bash
cd portfolio
source python3-virtualenv/bin/activate
flask run --host=0.0.0.0' > start-flask.sh
chmod +x start-flask.sh

tmux new-session -d -s flask_session './start-flask.sh'
