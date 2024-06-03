# 1. Commands

- Show all databases `SHOW DATABASES;`

- Create a new database: `create database <your_database_name>;`

- Use the new database: `use <your_database_name>;`

- Run sql file:
        
        SOURCE /path/to/your/script.sql;
        mysql --host=127.0.0.1 --port=3306 --user=root --password <your_password> < <your_sql_file.sql>;

- To list all the tables names from the database, use the command below in the terminal:

        SHOW TABLES;
        SHOW FULL TABLES WHERE table_type = 'BASE TABLE';

- Clear mysql terminal: `Ctrl + L`

- Explore the structure of the table: `DESCRIBE <your_table>;`

- Query `SELECT * FROM <your_table>;`

- Finally, dump/backup the staff table from the database using the command below in the terminal:

        mysqldump --host=127.0.0.1 --port=3306 --user=root --password <your_database> <your_table> > <your_sql_file.sql>

- To see a list of the Storage Engines supported on your MySQL server: `SHOW engines;`

- Create new user: `CREATE USER <your_user>`

- Quit `\q`

# 2. Configuration, storage Engines, and system Tables

The MySQL server contains a database called mysql. This is the system database that contains information required for the server to run, such as meta data on all the other tables in the database. This database is one of the special cases where the default InnoDB storage engine is not used. Instead, the tables in the mysql database used the MyISAM storage engine. In general, we mostly query the system tables and rarely modify them directly.

The tables in the mysql database fall into several categories, some of which include:

- Grant System Tables
- Object Information System Tables
- Log System Tables
- Server-Side Help System Tables

For your reference, an exhaustive list of the categories can be found in Section 5.7 of the MySQL documentation.

# 3. Grant System Table Category

Let’s take a deeper look at the `Grant System Table category`. They contain information about the user accounts and the privileges granted to them.

1. First, let’s see all the databases on the MySQL server by entering the following command into the CLI: `SHOW DATABASES;`

2. Now connect to the mysql data by entering: `SHOW TABLES;`

3. The user table contains user accounts, global privileges, and other nonprivilege columns. There are many columns in this table and is a little unwieldy to look at so let’s take a look at just the first column which lists the names of the users in the database. Enter the following into the CLI: `SELECT User from user;`

# 4. Query the `INFORMATION_SCHEMA` Database Tables

1. The `INFORMATION_SCHEMA` is a database found inside every MySQL server. It contains meta data about the MySQL server such as the name of a database or table, the data type of a column, or access privileges. Note that this database contains read-only tables, so you cannot directly use any INSERT, UPDATE, or DELETE commands on them. Let’s go ahead and connect to the database.


2. In the information_schema database, there exists a table called `COLUMNS` which contains meta data about the columns for all tables and views in the server. One of the columns in this table contains the names of all the other columns in every table. Let’s go ahead and look at the names of the columns in the `country` table in the `world` database by entering the following command in the CLI:

        SELECT COLUMN_NAME FROM COLUMNS WHERE TABLE_NAME = 'country';

3. Another point of interest in the information_schema database is the TABLES table which contains meta data about all the tables in the server. One of the columns in this table contains information about a table’s storage engine type. To tie this back to our earlier discussion about storage engines, run the following command in the CLI to view the storage engine type for the ‘country’, ‘city’, ‘countrylanguage’, and finally the ‘csv_test’ table you created:

        SELECT table_name, engine FROM INFORMATION_SCHEMA.TABLES 
        WHERE table_name = 'country' OR table_name = 'city' 
        OR table_name = 'countrylanguage' OR table_name = 'csv_test';

4. Finally, the TABLES table in the information_schema database contains information on the the size of a given table in bytes. This information is stored in two columns: data_length and index_length which stores the size of the data in the table and the size of the index file for that table, respectively. Therefore, the total size of the table is the sum of the values in these two columns. This value would be given in bytes, however, if you wish to use a more convenient unit, the sum can be converted to kB by dividing by 1024. You can find the size of the tables (in kB) you queried in the previous step with the following command in the CLI:

        SELECT table_name, (data_length + index_length)/1024 FROM INFORMATION_SCHEMA.TABLES 
        WHERE table_name = 'country' OR table_name = 'city' 
        OR table_name = 'countrylanguage' OR table_name = 'csv_test';

# 5.Transaction logs for recovery