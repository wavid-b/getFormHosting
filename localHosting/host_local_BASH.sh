#!/bin/bash
# Check if main.py and getForm.py in src folder
if [ ! -f "./src/main.py" ]; then
    echo "main.py not found in src folder. Exiting..."
    exit 1
fi
if [ ! -f "./src/getForm.py" ]; then
    echo "getForm.py not found in src folder. Exiting..."
    exit 1
fi
# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python not found. Installing Python..."
    sudo apt-get update
    sudo apt-get install -y python3
else
    echo "Python is already installed."
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Pip not found. Installing Pip..."
    sudo apt-get install -y python3-pip
else
    echo "Pip is already installed."
fi

echo "Pyton and pip installed"

#install dependencies
echo "Installing dependencies..."
#installing pandas
sudo pip3 install pandas
#installing numpy
sudo pip3 install numpy
#installing flask
sudo pip3 install flask
#installing unidecode
sudo pip3 install unidecode

#run the main.py function
python3 ./src/main.py

#open the browser to localhost:8000
echo "Opening browser to app"
xdg-open http://localhost:8000