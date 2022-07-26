# courses-circleci-python-example
Example of a simple Python application to demonstrate the use cases of CircleCI 

This application consists of: 

- A simple Flask webserver with one endpoint 
- One HTML page printed when the Flask endpoint is called
- Use of env variables to manage different environments
- Setup of linter and prettier 
- Test method 

## How to run the application ? 

Create a venv to install the dependencies locally when you'll run the application

`mkdir envs/` <br />
`python3 -m venv envs/<your_env_name>`

Then activate the environment 

`source envs/<your_env_name>/bin/activate`

Navigate to the folder src then install the dependencies

`cd src` <br />
`pip install -r requirements.txt`

You should now be able to run the flask application ! 
Choose an environment name if you want to, but that's not mandatory.  

`ENV_NAME=<my_env> FLASK_APP=main:flask_engine flask run`

## Run the tests 

#### pytest

You can run the tests using the command: `pytest`

## Linter check and fix

#### pylint

The check of code style is done by <b>pylint</b>, run: `pylint src` or `pylint .` if it does not work. 

#### black

The style corrections made to the code are done by <b>black</b>, run: `black .` or `black src` if it does not work.