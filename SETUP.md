# Setup

## MySQL Database

- This application maintains MySQL to maintain user data. Users can use the
  MariaDB as an alternate to MySQL.
- If a preexisting MySQL database is available, you skip the following steps
  and use your database server.
- User can a setup MySQL server using docker. Ensure that you have "Docker Desktop"
  software installed.
- An example docker-compose file that can be used by the user is provided in
  the docker folder. 
- User can open a command prompt/shell in the docker folder and run the
  following command:
  
  docker-compose up -d

- This launches the mysql and adminer services in detached mode. Refer the
  docker and docker-compose documentaton for details on docker usage.

## Application Interface Configuration

- Edit the config.txt and replace the *user-name*, *user-password* and
  *db-name* values with the appropriate MySQL database values.
- In case of using the *docker-compose.yml* file provided with the repository,
  the following values should be used:
  - *user-name*: *${MYSQL_USER}*
  - *user-password*: *${MYSQL_PASSWORD}*
  - *db-name*: *${MYSQL_DATABASE}*

## Setup Python environment

- Create a python virtual environment
- Install python package requirements using

  pip install -r requirements.txt

- Activate python virtual environment

## Initialize database

- Configure the database connection using the following command.

  python config.py

- Initialize the database and create admin user using the following command.

  python initdb.py [admin-email] [admin-password]

- Here, user needs to provide the appropriate values for *admin-email* and
  *admin-password*.
- This will create an admin user for logging in and administrating other
  users.

## Start the Dash application

- Start the dash application using the following command.

  python index.py

- Login as admin using the previously defined password, go to admin page and
  create the required user accounts.
