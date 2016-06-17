# Neo4j Movies Example Application
Displaying data in a table with search

## Stack

* Neo4j server
* Flask

## Setup

Setup an environment for the app:

```
$ virtualenv env
$ source env/bin/activate
```

Install dependencies:

```
$ pip install -r requirements.txt
```

## Run locally

The movies database is available in Neo4j by defauls.
Open Neo4j browser at http://localhost:7474
Type: :play movies, click at the statement and then click run.

Start up a Flask web server in terminal:

```
$ python app.py
```

Navigate to http://localhost:8080 to see your application.
