# commands

- Show all databases `SHOW DATABASES;`

- Create a new database: `create database <your_database_name>;`

- Use the new database: `use <your_database_name>;`

- Run sql file:
        
        SOURCE /path/to/your/script.sql;
        mysql --host=127.0.0.1 --port=3306 --user=root --password <your_password> < <your_sql_file.sql>;

- To list all the tables names from the database, use the command below in the terminal: `SHOW FULL TABLES WHERE table_type = 'BASE TABLE';`

- Clear mysql terminal: `Ctrl + L`

- Explore the structure of the table: `DESCRIBE <your_table>;`

- Query `SELECT * FROM <your_table>;`

- Finally, dump/backup the staff table from the database using the command below in the terminal:

        mysqldump --host=127.0.0.1 --port=3306 --user=root --password <your_database> <your_table> > <your sql file.sql>

- quit `\q`
