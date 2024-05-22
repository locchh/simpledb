# commands

- get help:  `help`

- show data directory `SHOW data_directory`

- get all databases `\l`

- quit `\q`

- connect to specific database `\c <your_database>`

- list all tables `\dt`

- list all tables and views `\dp`

- get columns from specific table `\d <your_table>`

- To dump/backup the store table from the database:

        pg_dump --username=root --host=localhost --password --dbname=<your_database> --table=store --format=plain > <your dump file>

# deploy Amazon RDS (free-tier)

# deploy Amazon EC2