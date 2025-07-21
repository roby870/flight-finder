# Code Challenge

## Overview

Implement an API in FastAPI that:




## Requirements

- [Docker](https://www.docker.com/) (recommended version: 20.10 or higher).
- [Docker Compose](https://docs.docker.com/compose/) (recommended version: 2.0 or higher).

## .env file

This file contains the environment variables needed to run the application. As a template, we have included a .env.example file. Copy this file and rename it to .env. You can customize the database configuration and other environment variables according to your needs. Example values are provided.

## Ports

The application is exposed on port 8000, and the PostgreSQL database on port 5432 (for the application) and 5433 (for testing).

## How to run the application

Once you have cloned the repository, run `docker-compose build` in the root directory of the project and then `docker compose up app`. If you don’t want to see the output in the terminal and prefer to run in the background, you can execute `docker compose up -d app`.

## Using Swagger

Once the application is up and running, you can test the API using Swagger. Swagger provides a graphical interface to interact with the API more easily.
Open your web browser and go to the following URL: http://localhost:8000/docs. On this page, you will find the automatically generated API documentation, and you will be able to test the available endpoints.

## Journey Seeds

There are some journeys seeds in the database. You can find them in the repository.py file.


## Tests

You can run tests with `docker-compose run test`

## Code Formatting and Linting with Pre-commit

This project uses [`pre-commit`](https://pre-commit.com/) to automatically format and lint Python code before each commit. It includes the following tools:

- **[Black](https://black.readthedocs.io/)** – a code formatter for enforcing style consistency.
- **[Pylint](https://pylint.pycqa.org/)** – a linter to identify code issues and enforce coding standards.

### 1. Install Pre-commit

Make sure you have Python (≥ 3.7) installed on your local machine, then install `pre-commit` globally:

```bash
pip install pre-commit
```

### 2. Install Pre-commit Hooks

Navigate to the root directory of the project and run:

```bash
pre-commit install
```

### 3. Run Pre-commit

Pre-commit will automatically format and lint your code before each commit. If there are any issues, you will need to fix them before the commit can be completed.
