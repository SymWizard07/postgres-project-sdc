# How to use this demo  
## 1. Install Docker  
https://www.docker.com/get-started/  
After completing the install, be sure to run the Docker Desktop application. It may require you to log out and into your computer.  
Ensure that the Docker Engine is running. You can confirm this by opening a terminal and running:  
`docker run hello-world`

## 2. Start the PostgreSQL Docker container
Navigate to the project directory containing the docker-compose.yml file, and run  
`docker-compose up -d`  
This will start the containerized PostgreSQL server. No database setup required!

## 3. Install Python dependencies (Optional)
The python requirements are already present in this project, but if it does not work for you, try running this command to install requirements.  
`pip install -r requirements.txt`

## 4. Run the Python script
`python app.py`  
This will add an entry to the table for a random number, and return every entry in the table every time the program is run. You can run it multiple times to see the table get bigger as more is added.

## 5. Stop the database when done
`docker-compose down`  
This will stop the running PostgreSQL server. Database info will be retained in the data directory, and can be modified again when the server is back online.

# Utility of Docker
Because of the nature of PostgreSQL, I decided to utilize the container function of Docker, which allows a machine to sandbox a section of itself to act as a network port.  
After completing this demo, please consider using Docker in your own projects, as it is a particularly powerful tool that allows testing of different applications before production.