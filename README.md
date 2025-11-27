# AI-README-CLI
[![GitHub](https://img.shields.io/badge/GitHub-theFoxCost/AI--README--CLI-ff69b4.svg)](https://github.com/theFoxCost/AI-README-CLI)

## Description
AI-README-CLI is a CLI-tool designed to generate high-quality, AI-generated README files with ease. This project aims to provide a simple and efficient way to create professional README files, saving developers time and effort.

## Tech Stack and Main Features
* Tech Stack:
	+ Python
* Main Features:
	+ Speed: Generate README files quickly and efficiently
	+ Free: Completely free to use
	+ Easy to use: Simple and intuitive interface

## Installation Instructions
To install AI-README-CLI, follow these steps:
```bash
# Install dependencies
pip install requests==2.32.5

# Clone the repository
git clone https://github.com/theFoxCost/AI-README-CLI.git

# Navigate to the project directory
cd AI-README-CLI

# Install the project using pip
pip install .
```

## Run Commands
To run AI-README-CLI, use the following command:
```bash
python main.py
```

## Environment Variables
To use AI-README-CLI, you need to set the following environment variable:
```bash
GROQ_API_KEY=API_KEY
```
Replace `API_KEY` with your actual API key.

## Project Type
AI-README-CLI is a CLI tool.

## Usage Examples
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
|-- templates/
|   |-- basic.py
|   |-- ...
|-- ...
```
The `templates` directory contains the different templates that can be used to generate README files.

## Screenshots / Demo Link
[![Demo](https://img.shields.io/badge/Demo-AI--README--CLI-ff69b4.svg)](https://github.com/theFoxCost/AI-README-CLI)

## Dependencies
AI-README-CLI depends on the following libraries:
* `requests==2.32.5`

## License
AI-README-CLI is licensed under the MIT License.

## Installation Requirements
To install AI-README-CLI, you need to have the following installed:
* Python
* pip
* uv
* venv

## Known Issues
There are no known issues with AI-README-CLI.

## Configuration Notes
There are no configuration notes for AI-README-CLI.

## API Routes
There are no API routes for AI-README-CLI.

## High-Level Project Overview
The high-level project overview of AI-README-CLI is as follows:
1. The user installs AI-README-CLI using pip.
2. The user sets the `GROQ_API_KEY` environment variable.
3. The user runs AI-README-CLI using the `python main.py` command.
4. AI-README-CLI generates a README file based on the user's input.
5. The user can customize the README file using different templates and options.