#!/bin/bash
echo "Welcome To AI README Generator"
sleep 1

echo "Building the Docker Image..."
sleep 1
docker build -t ai-readme-cli .
sleep 1
echo "Build Completed"
sleep 1

AUTO_RUN=false
for arg in "$@"; do
    if [ "$arg" = "-y" ]; then
        AUTO_RUN=true
    fi
done

if [ "$AUTO_RUN" = true ]; then
    choice='y'
else
    echo "Do you want to run your app (y/n)?"
    read choice
fi

if [ "$choice" = "y" ]; then
    sleep 1
    clear
    echo "Mounting a volume to persist files..."
    sleep 1
    docker run -it -v "$(pwd)/main:/app/main" ai-readme-cli
else
    echo "Aborting..."
    exit
fi
