# commands

1. Create a new database: `create database <your_database_name>;`

2. Use the new database: `use <your_database_name>;`

3. Run sql file:
        
        source /var/lib/mysql/<your_sql_file.sql>;
        mysql --host=127.0.0.1 --port=3306 --user=root --password <your_password> < <your_sql_file.sql>;

4. To list all the tables names from the database, use the command below in the terminal:

        SHOW FULL TABLES WHERE table_type = 'BASE TABLE';

5. Clear mysql terminal: `Ctrl + L`

6. Explore the structure of the table: `DESCRIBE <your_table>;`

7. Query `SELECT * FROM <your_table>;`

8. Finally, dump/backup the staff table from the database using the command below in the terminal:

        mysqldump --host=127.0.0.1 --port=3306 --user=root --password <your_database> <your_table> > <your sql file.sql>

8. quit `\q`