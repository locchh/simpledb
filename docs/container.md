# Deployment

## Pull docker image

- pull docker postgres: `docker pull postgres`

- pull docker mysql: `docker pull mysql`

- pull docker myphpadmin: `docker pull phpmyadmin`

- pull docker mongodb: `docker pull mongo`

## Run docker container postgres
- run docker postgres:

        docker run --name <your_container_name> \
        -e POSTGRES_USER=<your_user> \
        -e POSTGRES_PASSWORD=<your_password> \
        -p 5432:5432 \
        -v <your_local_full_path>:/var/lib/postgresql/data \
        -d \
        postgres

- access postgres container

        docker exec -it <your_container_name> bash
        docker exec -it <your_container_name> /bin/bash

- access psql: `psql -U <your_postgres_user> -W`

## Run docker container mysql
- create network: `docker network create <your_network>`

- run docker mysql:

        docker run --name <your_container_name> \
        --network <your_network> \
        -e MYSQL_ROOT_PASSWORD=<your_password> \
        -v <your_local_full_path>:/var/lib/mysql \
        -p 3306:3306 \
        -d \
        mysql

- access mysql container: `docker exec -it <your_container_name> bash`

- Connect to the client as a root user: `mysql -u root -p`

- run docker myphpadmin:

        docker run --name <your_container_name> \
        --network <your_network> \
        -e PMA_HOST=<your_mysql_server> \
        -p 8081:80 \
        -d \
        phpmyadmin

*Note: `PMA_HOST` mysql server ip address, or mysql server container (sample network)*

- access myphpadmin: `http://localhost:8081/`

## Run docker container mongodb
- run docker mongodb:

        docker run --name <your_container_name> \
        -v <your_local_full_path>:/data/db \
        -p 2717:27017 \
        -d \
        mongo

- access mongo container: `docker exec -it <your_container_name> bash`

- Connect dbms:

        mongosh
        mongo