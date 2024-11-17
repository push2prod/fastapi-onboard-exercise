# FastAPI Server - Exercises for CSV Handling and Async API Requests

Welcome to the FastAPI server repository! This repo is designed to guide you through two exercises related to handling CSV files with Polars and making asynchronous requests to APIs. You'll be working with Python 3.11 and FastAPI, and we've included a Docker Compose file to help you spin up the server quickly.

## Prerequisites

Before you start, make sure you have the following installed:

- **Python 3.11** (or later)
- **Docker** (for Docker Compose)
- **Docker Compose**

If you don't have these tools installed, you can follow the official documentation to get them set up:

- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

The project is organized as follows:

```
.
├── app/
│   ├── __init__.py        # Initialization file for the app package
│   ├── docker-compose.yml # Docker Compose configuration
│   ├── Dockerfile         # Dockerfile for building the app container
│   ├── main.py            # FastAPI server entry point
│   ├── models/            # Pydantic models for schema validation
│   │   ├── flights.py     # Models for flights data
│   │   └── jokes.py       # Models for jokes data
│   ├── routers/           # Routers for handling API endpoints
│   │   ├── exercise_1.py  # Router for exercise 1 (CSV handling)
│   │   └── exercise_2.py  # Router for exercise 2 (Async API requests)
│   ├── services/          # Business logic and helper functions
│   │   ├── exercise_1.py  # Service functions for exercise 1
│   │   ├── exercise_2.py  # Service functions for exercise 2
│   │   └── lifespan.py    # Lifespan function to handle server startup/shutdown
│   └── etc/               # Miscellaneous files, including requirements.txt
│       └── requirements.txt # Python dependencies for the project
```

## Setup

To get started, clone the repository and install the dependencies:

```bash
git clone https://github.com/push2prod/fastapi-onboard-exercise.git
cd fastapi-onboard-exercise
```

### Install dependencies

First, set up a Python virtual environment and install the required libraries:

```bash
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
pip install -r app/etc/requirements.txt
```

### Run the server with Docker Compose

We have provided a `docker-compose.yml` file to easily start the server.

To start the server and client, run the following:

```bash
docker-compose up --build
```

Once the server is running, you can access the FastAPI Swagger documentation at:

```
http://localhost:8000/api/docs
```

## Exercises

### 1. CSV File Handling with Polars

In `app/routers/exercise_1.py`, you will find a function placeholder for reading and processing CSV files using [Polars](https://pola-rs.github.io/polars-book/). Polars is a fast DataFrame library that can handle large datasets efficiently.

#### Task:
- Implement a function that reads a CSV file into a Polars DataFrame and performs basic operations like filtering, grouping, or transforming the data. You can use Polars' [documentation](https://pola-rs.github.io/polars-book/) to learn how to manipulate DataFrames.


### 2. Making Async Requests to APIs

In `app/services/exercise_2.py`, you will learn how to make asynchronous requests to external APIs using FastAPI's `httpx` integration. Async I/O allows FastAPI to handle multiple requests concurrently, making it more efficient.

#### Task:
- Implement a function that fetches data from an external API asynchronously using the `httpx` library. You'll find an API endpoint in `app/routers/exercise_2.py` where you need to implement the functionality.


For more information about FastAPI's async capabilities, check out the [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/async/) and [httpx](https://www.python-httpx.org/).

---

## Testing Your Implementation

Once you have implemented both exercises you can test all endpoints using Swagger UI available at [http://localhost:8000/api/docs](http://localhost:8000/api/docs).


## Learning Resources

To help you complete the exercises, here are some references to get you started:

### Polars
- [Polars Book](https://pola-rs.github.io/polars-book/)
- [Polars Documentation](https://pola-rs.github.io/polars/)

### FastAPI & Async I/O
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Async Programming in Python](https://realpython.com/async-io-python/)
- [httpx Documentation](https://www.python-httpx.org/)

## Good Luck!

We hope you enjoy working on these exercises and learn a lot about FastAPI, Polars, and asynchronous programming in Python. If you encounter any challenges or have questions, don't hesitate to refer to the documentation or reach out for help.

Good luck and happy coding! 🚀
