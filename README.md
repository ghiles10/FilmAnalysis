# FilmAnalysis

## Presentation
This project aims to collect data on movies from different websites using the web scrapping technique.The data is transformed using pyspark. This data is then presented to the user via a user interface built with Flask. The user can choose a movie and display the associated data.

The project is deployed in a Docker container by creating a Dockerfile image. This makes it easy to install and run the project on any computer with Docker.

The app is hosted on the local machine at http://localhost:5000

## project structure 

### webscraping 

Data recovery from the AlloCiné website : https://www.allocine.fr/

### Database 

Use of pyspark to clean the data and build a compact database

### Web Application

this project includes a user interface developed with Flask that asks the user to enter a movie title. This interface uses the HTTP POST method to query the database through PySpark and displays the results to the user.

### DockerFile

A Dockerfile image has been built which gathers all the elements of our project and which allows to run it in a Docker container.

## Getting Started

If you are on a Linux operating system, please follow these steps to install and run the project

`cd FilmAnalysis/notebook`

`bash install.sh`

`bash launch.sh`

