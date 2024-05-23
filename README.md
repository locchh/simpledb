# simpledb
example of simple database

- database name: `example`
- user: `root`
- password: `simple_pass`

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

|No|Task|`psql`|`mysql`|`mongo`|`sqlite`|
|---|---|---|---|---|---|
|01|Getting Started with Command Line|✅|✅|✅|❌|
|02|Create Tables and Load Data|✅|✅|❌|❌|
|02|Keys and Constraints|✅|✅|❌|❌|
|03|View, Procedure|✅|✅|❌|❌|
|04|Configuration and System|✅|✅|❌|❌|
|05|Transaction Logs for Recovery|❌|❌|❌|❌|
|06|Backup and Restore|✅|❌|❌|❌|
|07|User Management and Access Control|❌|❌|❌|❌|
|08|Monitoring and Optimizing your Databases|❌|❌|❌|❌|
|09|Troubleshooting|❌|❌|❌|❌|
|10|Automating Tasks using Shell Scripts|❌|❌|❌|❌|
|11|APIs|✅|✅|❌|✅|

# references

https://docs.sqlalchemy.org/en/14/orm/tutorial.html

https://faker.readthedocs.io/en/master/
