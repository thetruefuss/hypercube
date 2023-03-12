# hypercube

hypercube is a search interface for searching IT ebooks built with Python using the Django Web Framework.
Get the books crawler at [https://github.com/thetruefuss/books-scraper](https://github.com/thetruefuss/books-scraper)

### Installation Guide

Clone this repository:

```shell
$ git clone https://github.com/thetruefuss/hypercube.git
```

Install requirements:

```shell
$ pip install -r requirements.txt
```

Copy `.env.example` file content to new `.env` file and update the credentials if any.

Run Django migrations to create database tables:

```shell
$ python manage.py migrate
```

Run the development server:

```shell
$ python manage.py runserver
```

Verify the deployment by navigating to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your preferred browser.
