## High Level Purpose Statement
I want to figure out how to get a PostgreSQL server running locally, and add and query data to and from a database.

## Experimental Design
Because PostgreSQL is so new to me, I'd like to test it out using python. I need to find a good library to interact with the database using it. I want this python script to be repeatable, to show that the database information is stored not just in a program, and that it can be added to and queried easily between executions. Lastly, I want the PostgreSQL server to run locally without much overhead for the person testing the demo. I will use docker to create a containerized instance for this purpose.

## Resources Available
Documentation for PostgreSQL, documentation for Docker. AI will also be a helpful tool for getting the project started.

## Time Estimate
I will spend around 7-8 hours on this project, although the demo is small. I will mostly be wading through documentation on setting up the Postgres server and using it with Docker, with the last couple hours making sure the python code and library work properly.

## Experiment Notes
Docker made testing Postgres signifigantly easier via the container. It was like I was connecting to a server, but it took care of all the overhead for me. PostgreSQL isn't too different from other types of SQL I have used in the past either, which made it easy to add data. The Python library for interacting with the Postgres server also had a smooth implementation.

## Results
The PostgreSQL server runs smoothly in a dockerized container. The Python script can be executed any number of times to demonstrate how the database works. Shutting down the server saves data as well, and starting it up after closing it is relatively easy to do.

## Consequences for the Future
PostgreSQL syntax was very easy to use compared to what I've done in the past, and connecting to the database was easy as well. If I ever work on a larger project where I feel like I would need a database, I might use this service. Other than PostgreSQL, I was extremely impressed with Docker's capabilities and clean UI. It made it easy to rapidly set up the demo server for Postgres. I would definitely use this again should I ever need to.