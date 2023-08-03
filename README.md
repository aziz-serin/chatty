# CHATTY

## What is this app?

This app allows you to use the features of OpenAI's Chat-GPT, including having a memory between conversations (Within the
supported token limits of the model used). You can also use the capabilities of Google's text to speech APIs as well as OpenAI's
speech to text API, whisper.

## Structure of the application

The app is divided into 3 parts, a python/flask based back-end and svelte based front end, and a mongodb database. 
The front-end does not talk to any other API other than the back-end at the current version of this application.

## Prerequisites for running the application

You will need a Google Cloud account with text to speech service enabled, as well as an OpenAI api key to make the queries
to their apis. If you did set up [gcloud](https://cloud.google.com/sdk/gcloud) locally before, you should have a directory called .config/gcloud in your home directory, 
there will be a file called 
```application_default_credentials.json```
in that directory. You can copy it to the root of this project since it is already git ignored, or edit the 
````chatty.env```` and point it to your file. You should also set OpenAI's API key in the same .env file.

## How to run the application

Due to the fact that I am using a mongodb database, easiest way to run the app is using docker. You can use docker compose
to run everything by using
```shell
docker compose up
```
or to build e.g. after making some small changes.
```shell
docker compose up --build
```
You can bring down the containers by using
```shell
docker compose down
```
or to clean up the database by removing the volumes.
```shell
docker compose down --volumes
```
You can also run this to clean everything -including the containers-
```shell
docker compose down --remove-orphans --volumes
```
### How to work on the back-end

* Set the working directory as the root of the project
* Install poetry if you do not have it already by using ```pip``` or your preferred python dependency manager, and run the followig:
```shell
pip insall poetry
```
* After completing the above step, run this to install the application dependencies. 
```shell
poetry install
```
* Set up ```GOOGLE_APPLICATION_CREDENTIALS```, ```OPENAI_API_KEY```, and ```PYTHON_BUFFERED``` env variables locally 
or as part of your venv. You can do this just by sourcing the chatty.env file instead of doing each of these individually.
* You need to also set up your ```PYTHONPATH``` env variable. You can do so by:
```shell
export PYTHONPATH="${PYTHONPATH}:/chatty/src"
```
* You will need a mongodb db running at the same time while working with the backend. You can do so by running one locally
(not recommended), or spin up only the mongodb service as part of the docker compose like below.
```shell
docker compose up -d mongodb_container
```
* Now you can run the application by running
```shell
poetry run python src/va.py
```
* Then you can use the included small postman collection [here](Chatty.postman_collection.json) or run the front-end
application to see/test your changes. To run a frontend you can spin up the frontend service as shown above with the mongodb 
service.
* The mongodb password is set in [docker-compose.yml](docker-compose.yml) file, as part of the mongodb service. If you change those values
as well as anything that interest the backend application, you will also need to update the [config.ini](src/va/resources/config.ini)
file, this is the file-based config for the application. 

### How to work on the front-end
* Spin up the back-end application and the database by using this command or locally by following the 
[previous section](#how-to-work-on-the-back-end)
```shell
docker compose up -d mongodb_container va
```
* Navigate to src/ui directory, and run below to install the dependencies of the application.
```shell
npm install
```
* Then run below to start the front-end application on development mode.
```shell
npm run dev
```

### NOTES
Feel free to fork this repo or clone it, and just play with it! This repo can also help you cut your Chat-GPT premium cost,
it uses gpt-3.5 model, but you can use this website by running it locally and save $20 a month! I know my js and front-end
skills are not the best, so feel free to leave any comments/suggestions by reaching out to me!