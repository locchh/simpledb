# commands

- get help:  `help`

- show data directory `SHOW data_directory`

- get all databases `\l`

- quit `\q`

- connect to specific database `\c <your_database>`

- list all tables `\dt`

- list all tables and views `\dp`

- get columns from specific table `\d <your_table>`

# deploy Amazon RDS (free-tier)

1. Search `RDS`
2. Select `create database`
3. Choose a database creation method: `Standard create`
4. Engine options: `PostgreSQL`
5. Engine options.Engine Version: optional
6. Templates: `Free tier`
7. Settings.DB instance identifier `your_database_instance_name`
8. Settings.Master username: `your_master_user_name`
8. Settings.Master password: `your_password`
9. Instance configuration.DB instance class: `db.t3.mirco`
10. Storage.Storage type: `General Purpose SSD (gp2)`
11. Storage.Allocated storage: 20
12. Storage.Allocated storage.Enable storage autoscaling: disable
13. Connectivity.Compute resource
14. Connectivity.Virtual private cloud (VPC): default
15. Connectivity.DB subnet group: default
16. Connectivity.Public access: Yes (No->Only VPC can access)
17. Additional configuration.Database port: 5432
18. Database authentication: Password authentication
19. Additional configuration.Database options.Initial database name: optional
20. Additional configuration.Database options.Backup: disable
21. Additional configuration.Database options.Encryption: disable
22. Create database
23. Copy endpoint and port to access


# deploy Amazon EC2