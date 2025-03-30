# Creature Data Scraper

This is an interview project and is a data scraper designed to retrieve information about creatures. It currently supports APIs for Digimon and Pokemon. The project is implemented using Python and the Django Framework, utilizing Python version 3.7.16 and Docker.

## Installation

Before starting the project, please ensure that you have Python 3.7.16 and Docker installed on your system. Follow these steps to set up the project:

1. Clone the project repository to your local machine.
2. Navigate to the project root directory.
3. Create a `.env` file in the project root. This file should contain the necessary information, such as database credentials, required for the project. Below is an example .env file. Anything in [] can be replaced with whatever variables you like.
```
ENVIRONMENT=dev

DJANGO_SETTINGS_MODULE=config.settings

DJANGO_SECRET_KEY=[your_secret]

MYSQL_ROOT_PASSWORD=[your_root_password]

MYSQL_DATABASE=[your_database]
MYSQL_USER=[your_admin]
MYSQL_PASSWORD=[your_password]
MYSQL_DATABASE_HOST=mysql-db
MYSQL_DATABASE_PORT=3306

```
4. Run `docker compose up` which will build the container and start up the application.
5. Run database migrations using `docker compose exec app python creaturescrape/manage.py migrate` 

## Usage

To use the project, follow these steps:

1. After starting the project, open your web browser and access the URL `localhost:8000/creatures/` to access the simple frontend that utilizes the API.
2. The quickest API to consume is the Digimon API, which allows you to retrieve a large batch of Digimon at once.
3. For the Pokemon API, since it has a nested hierarchy, multiple calls are required to obtain the full information of a Pokemon. The root endpoint of the Pokemon API provides the total number of Pokemon entries, allowing us to construct batches to retrieve a large amount of Pokemon data at once.

## Ingesting Data

```
localhost:8000/creatures/ GET
```
This opens up a webpage that lets you ingest Pokemon or Digimon APIs by posting to the API endpoints

```
localhost:8000/creature-list/ GET
```
This opens up a list of all Scraped creatures. Mouse over one of their photos!

```
localhost:8000/creature-list/<str:creature_type>/<str:trait>/<str:trait_value>/ GET
```
This filters the list by a creature type (Pokemon or Digimon) a trait (Level, Type1, Type2) and a value related to that trait (Rookie, Electric, Fire)
Returns a similar page to the previous API endpoint

```
localhost:8000/ingest/digimon POST
```
Ingests the Digimon API returns the amount of new Creatures Ingested

```
localhost:8000/ingest/pokemon/ POST
```
Ingests the Pokemon API. By default it will attempt to Ingest everything. This can be limited by sending an offset and a limit as post data.

## Ingestion Functions

In addition to the Endpoints you can also Ingest from the shell with objects in `creatures.utils`

```
ingest_creature_api
```

This is a data ingestor module that aims to be ready in case a new Creature type appears

```
full_scrape_pokemon_api
```
The pokemon API doesn't allow for batch getting of Creatures. Splitting the large amount of queries into batches is more for organization reasons

```
partial_scrape_pokemon_api
```

This basically takes a slice from the Pokemon API gathers all the URLs and then builds the data object to be translated into a model

```
scrape_digimon_api
```

This scrapes the Digimon API for Name Level and Images



