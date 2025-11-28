# README-AI-CLI
[README-AI-CLI](https://api.github.com/repos/theFoxCost/AI-README)

## Description
The README-AI-CLI is a tool designed to generate high-quality README files for GitHub repositories, powered by AI. This innovative solution aims to simplify the process of creating well-structured and informative README files, saving developers time and effort. With its lightweight and easy-to-use design, the README-AI-CLI is an ideal solution for anyone looking to improve their repository's documentation.

## Tech Stack and Main Features
* Tech Stack:
  + Python
  + Docker
  + Bash
* Main Features:
  + Really fast and works anywhere thanks to Docker containerization
  + Easy to use: just run `app.sh` and follow the instructions
  + Lightweight

## Installation Instructions
To get started with the README-AI-CLI, follow these simple steps:
```bash
# Clone the repository
git clone https://github.com/theFoxCost/AI-README.git

# Run the app.sh script
bash app.sh
```
Follow the instructions provided by the script to complete the installation.

## Run Commands
To run the README-AI-CLI, use the following commands:
```bash
# Give execute permission to the app.sh script
chmod +x app.sh

# Run the app.sh script
./app.sh
```

## Environment Variables
The README-AI-CLI uses the following environment variable:
* `GROQ_API_KEY`: (required for API interactions)

## Project Type
The README-AI-CLI is a Command-Line Interface (CLI) tool designed to generate README files for GitHub repositories.

## Usage Examples
<<<<<<< HEAD
Here are some examples of how to use AI-README-CLI:
* Generate a basic README file:
```bash
python main.py --basic
```
* Generate a README file with a specific template:
```bash
python main.py --template=<template_name>
```
Replace `<template_name>` with the name of the template you want to use.

## File Structure
The file structure of AI-README-CLI is as follows:
```markdown
AI-README-CLI/
|-- main.py
|-- main/
|   |-- {project_name}/
|   	|-- README.md	<-- the main (genrated by ai) file
|   	|-- Payload.md	<-- all info that sends to the GROQ API
|   	|-- Prompt.md	<-- my prompt (you can customise it make t much better)
|   	|-- github.json	<-- your github repo DATA is fetched and stored here  

|-- ...
```
The `templates` directory contains the different templates that can be used to generate README files.

## Screenshots / Demo Link
[![Demo](https://img.shields.io/badge/Demo-AI--README--CLI-ff69b4.svg)](https://github.com/theFoxCost/AI-README-CLI)
=======
Let the AI generate a README file for your repository. Simply run the `app.sh` script and follow the instructions to create a high-quality README file.
>>>>>>> cd2c24e (Added: Docker containerisation for the App and add Bash Script for automation)

## Dependencies
The README-AI-CLI relies on the following dependencies:
* Docker:latest
* Code editor (to view the generated README file)
* Python:latest (included in the Docker container)

## License
The README-AI-CLI is released without a license.

## High-Level Project Overview
<<<<<<< HEAD
The high-level project overview of AI-README-CLI is as follows:
1. The user installs AI-README-CLI using pip.
2. The user sets the `GROQ_API_KEY` environment variable.
3. The user runs AI-README-CLI using the `python main.py` command.
4. AI-README-CLI generates a README file based on the user's input.
5. The user can customize the README file using different templates and options.
### **WARNING: you may Still modify the README File**
=======
The README-AI-CLI uses a combination of natural language processing (NLP) and machine learning algorithms to generate high-quality README files. The tool is designed to be easy to use and provides a simple, intuitive interface for users to input their repository information and generate a README file. The generated README file includes all the necessary sections and content to provide a comprehensive overview of the repository.
>>>>>>> cd2c24e (Added: Docker containerisation for the App and add Bash Script for automation)
