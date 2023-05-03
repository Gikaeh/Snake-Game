# DevOps-Final-Project
Final project for CS333 - DevOps

# Project Overview
This repository is for a game like the classic snake game that will rum within you terminal. It uses pytimedinput to allow for an input within a certain set time (.4 secs default). The aim of the game is to move around the snake grabbing the food that shows up ($ default) in order to grow the body; you lose if you run into the wall or your own body.

# Directions to Run Program
- From the DockerHub library pull the latest image using the command (docker pull gikaeh/snake-game:latest)
- Run the Docker image using the command (docker run -i gikaeh/snake-game:latest)

# Pipeline Overview
Once a new update is pushed to github through a pull request to the main branch, a workflow is started that runs the test.py containing the unittest and intergrationtest. Once this is completed and if successful it then starts another workflow that builds and pushs the new image to the DockerHub project under the tag latest.

# CI/CD and Deployment Tools
- Unittest: Module used for testing in python

- Git: Used for version contol of code repository

- Github Actions: Used for pipeline of testing and pushing to docker

- Docker: Used for public deployment through DockerHub