# Catching A Phish - team19

A serious game to teach people to thwart phishing attacks. 
Web application by Kayra Yildiz, Jasveer Singh, Jessie Singh, David Wang, Ash Fernandes


Project management: https://trello.com/b/quQhCHD0/scrum-board
Github: https://github.com/kayrayildiz/COMPSCI-399-Project-Team19

This repository contains an implementation of an interactive web-based quiz game to teach people how to avoid falling for Phishing attacks.
It also contains unit tests which can be run through pytest.
It also contains a simple Flask application which renders content of User objects which are added to our domain model via an SQL database.

**Technologies used**
This repository contains a web-based game application built upon a Flask framewrok.
> **Front End technologies**: CSS, HTML, Jinja, Semantic UI design libraries: [https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css]
> **Back End technologies**: Flask, Python, SQL, Pytest

## Installation

**Installation via requirements.txt**

```shell
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm for requirements installation, set the virtual environment using 'File'->'Settings' and select your project from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 
Please use Python version 3.6 or newer versions for development.

## Execution of the web application

**Running the Flask application**

From the project directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 

## Testing with the pytest unit tests

After you have configured pytest as the testing tool for PyCharm (File - Settings - Tools - Python Integrated Tools - Testing), you can then run tests from within PyCharm by right-clicking the tests folder and selecting "Run pytest in tests".

Alternatively, from a terminal in the root folder of the project, you can also call 'python -m pytest tests' to run all the tests. PyCharm also provides a built-in terminal, which uses the configured virtual environment. 

````shell
$ python -m pytest tests
````

* Note that for some computers you may need to use python3