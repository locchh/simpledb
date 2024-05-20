# simpledb
simple database `sample_data`

**PERSONS**
|No|Column|Type|Constraint|
|---|---|---|---|
|01|person_id|int| primary key|
|02|first_name|varchar(100)|not null|
|03|last_name|varchar(100)|not null|
|04|birth_day|date|not null|
|05|email_address|varchar(150)|not null, unique|
|06|local_address|varchar(200)||

# summary

|No|Task|`psql`|`mysql`|`sqlite`|`mongo`|
|---|---|---|---|---|---|
|01|Getting Started with Command Line|[✅]()|❌|❌|❌|
|02|Create Tables and Load Data|❌|❌|❌|❌|
|02|Keys and Constraints|❌|❌|❌|❌|
|03|View, Procedure|❌|❌|❌|❌|
|04|Configuration and System|❌|❌|❌|❌|
|05|Backup and Restore|❌|❌|❌|❌|
|06|User Management and Access Control|❌|❌|❌|❌|
|07|Monitoring and Optimizing your Databases|❌|❌|❌|❌|
|08|Troubleshooting|❌|❌|❌|❌|
|09|Automating Tasks using Shell Scripts|❌|❌|❌|❌|
|10|APIs|❌|❌|❌|❌|

# references
https://faker.readthedocs.io/en/master/
