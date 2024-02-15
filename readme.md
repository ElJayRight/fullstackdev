# Outline

The goal is to have a full stack server that adds as a quick reference for code snippets. Everything will be hosted in AWS with only the front end being avaliable for the user. The use will be able to save code to the codebase server that will then be compiled and analysed against threatcheck. If the sample is opsec safe it will be added to a network share for download and use. If the sample fails there will be threatcheck output given back to the user along with the compiled sample.

To prevent large storage issues, samples will only be kept for 24hrs then deleted. The database of code snippets will be hosted privately and accessable via a ssh tunnel from the code server. All server modules shall be run within docker to help with compatibility.

Everything will be able to be spun up via ansible with the build files being stored in this repo.

# TechStack
Front end: Flask server

This will start out as an api to help with useability focusing around a terminal using `curl`. This could later be expanded to be a full website after a working beta is built


Database: MySQL

As the database will grow rapidly with each file added MySQL seems to be the right pick over sqlite3. There will be strict access to the database, as only the flask apis need to access it. The ability to add a file will also be done via a PUT request.


Codebase: GitLab Server

Due to familarity with the application it will be used to store the logic for the runners and code. The user will also be able to add project repos to this server, with artifact lifetime monitored to keep storage size at a minimum.


Compile server: Windows Server 2022

This should be a standalone server running multiple docker containers designed to complie project code. These containers are not perminate and will be deleted once the artifacts are generated.


Analysis container: Running on compile server.

There will be a seperate container that will anaylse the compiled sample against threatcheck and return the results as outlined above.

# Project Timeline
## Stage 1
Functioning Flask API and MySQL Server with the ability to view and add data.

Ansible scripts should also be created.

## Stage 2
Completed GitLab server with compile and analysis containers created.

Ansible and gitlab runner configs should be created.

## Stage 3
Create a working pipeline that will input a repo and output information on the compiled sample.

## Stage 4
Build out the flask frontend and stream line the creation of repos utilising the data stored in the database. (To be discussed at a later )


# Git Strategy
Each new feature shall be added as a feature branch, then merged with dev.

Once we validate there are no issues with the merge it shall be pushed to main.

# Future Ideas

A list of future things to be added once the scope is completed.