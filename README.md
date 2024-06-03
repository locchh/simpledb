# simpledb
example of simple database

- database name: `example`
- user: `root`
- password: `123`

**PERSONS**
|No|Column|Type|Constraint|
|---|---|---|---|
|01|person_id|int| primary key|
|02|first_name|varchar(100)|not null|
|03|last_name|varchar(100)|not null|
|04|gender|char|not null|
|05|birth_day|date|not null|
|06|email_address|varchar(150)|not null, unique|
|07|local_address|varchar(200)||

# summary

|No||
|---|---|
|01|Getting Started with Command Line|
|02|Import/Export|
|03|Query|
|04|View, Trigger, Function, Procedure|
|05|Configuration and System|
|06|Transaction Logs for Recovery|
|07|Backup and Restore|
|08|User Management and Access Control|
|09|Monitoring and Optimizing your Databases|
|10|Troubleshooting|
|11|Automating Tasks using Shell Scripts|
|12|APIs|

# references

[Faker](https://faker.readthedocs.io/en/master/)

[Sqlalchemy](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)

[MySQL Tutorial](https://www.mysqltutorial.org/)

[PostgreSQL Exercises](https://pgexercises.com/mys)

[PostgreSQL Tutorial](https://www.postgresqltutorial.com/)