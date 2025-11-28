#!/bin/bash
echo "Welcome To AI README Generator"
sleep 1

echo "Building the Docker Image..."
sleep 1

docker build -t ai-readme-cli .

sleep 1
echo "Building Complted"
sleep 1

echo "Do you Want To Run Your App (y/n)"
read choice

if [ $choice = 'y' ]; then
    sleep 1
    clear
    echo 'Mount a volume to persist files...'
    sleep 1
    docker run -it -v $(pwd)/main:/app/main ai-readme-cli
else
echo "aborting..."
    exit
fi
