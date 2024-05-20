# deployment

## pull docker image
- pull docker postgres: `sudo docker pull postgres`
- pull docker mysql: `sudo docker pull mysql`
- pull docker mongodb: `sudo docker pull mongo`

## run docker container postgres
- run docker postgres:

        docker run --name your_container_name \
        -e POSTGRES_USER=your_postgres_user \
        -e POSTGRES_PASSWORD=your_postgres_password \
        -p 5432:5432 \
        -v your_local_full_path:/var/lib/postgresql/data \
        postgres

- access docker-container

        docker exec -it your_container_name bash
        docker exec -it your_container_name /bin/bash

- access psql: `psql -U <your_postgres_user> -W`

## run docker container mysql
- run docker mysql:

## run docker container mongodb
- run docker mongodb:
