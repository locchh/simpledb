# 1. Commands

- Get help:  `help`

- Show data directory `SHOW data_directory`

- Get all databases `\l`

- Quit `\q`

- Connect to specific database `\c <your_database>`

- List all tables `\dt`

- List all tables and views `\dp`

- Get columns from specific table `\d <your_table>`

- To dump/backup the store table from the database:

        pg_dump --username=root --host=localhost --password --dbname=<your_database> --table=store --format=plain > <your dump file>

# 2. configuration, storage engines, and system tables

**Configure Your PostgreSQL Server Instance**

A PostgreSQL server instance has a corresponding file named `postgresql.conf` that contains the configuration parameters for the server. By modifying this file, you can enable, disable, or otherwise customize the settings of your PostgreSQL server instance to best suit your needs as a database administrator. While you can manually modify this `postgresql.conf` file and restart the server for the changes to take effect, you can also edit some configuration parameters directly from the command line interface (CLI).

In this exercise, you will customize the configuration settings for the PostgreSQL instance using the CLI.

1. First, let’s take a look at the current setting of the wal_level parameter. You can do so by entering the following command into the CLI. Without going into too much detail, the wal_level parameter dictates how much information is written to the write-ahead log (WAL), which can be used for continuous archiving. If you’re interested, you can find further information in the PostgreSQL official documentation.:

        SHOW wal_level;

2. The `ALTER SYSTEM` command is a way to modify the global defaults of a PostgreSQL instance without having to manually edit the configuration file. Let’s give it a try and change the `wal_level` parameter to `logical`. To change the parameter, enter the following command into the CLI:

        ALTER SYSTEM SET wal_level = 'logical';

3. When you executed the `ALTER SYSTEM` command in Step 2 of this exercise, a new file named `postgres.auto.conf` was created. You can open the file by first opening the file explorer on Cloud IDE then clicking `postgres > data > postgresql.auto.conf`.

**Navigate the System Catalog**

The system catalog stores schema metadata, such as information about tables and columns and internal bookkeeping information. In PostgreSQL, the system catalogs are regular tables in which you can add columns and insert and update values. In directly modifying the system catalogs, you can cause severe problems in your system, so it is generally recommended to avoid doing so. Instead, the system catalogs are updated automatically when performing other SQL commands. For example, if you run a CREATE DATABASE command, a new database is created on the disk and a new row is automatically inserted into the pg_database system catalog table, storing metadata about that database.

1. Start with a simple query of pg_tables, which is a system catalog containing metadata about each table in the database. Let’s query it to display metadata about all the tables belonging to the bookings schema in the demo database by entering the following command into the CLI:

        SELECT * FROM pg_tables WHERE schemaname = 'bookings';

2. Suppose as the database administrator, you would like to enable row-level security for the boarding_passes table in the demo database. When row security is enabled on a table, all normal access to the table for selecting or modifying rows must be specified by a row security policy. Since row security policies are not the focus of this lab, we will not go in depth about specifying a policy but will simply enable it for demonstration purposes. However, if you wish to learn more about this topic, you can check out the PostgreSQL documentation. To enable row security on the boarding_passes table, enter the following command in the CLI:
        ALTER TABLE boarding_passes ENABLE ROW LEVEL SECURITY;

3. Let’s connect your work in the previous section about PostgreSQL instance configuration to the system catalogs. Earlier, you used SHOW statements to display configuration parameters. There’s also a system catalog called pg_settings that stores data about configuration parameters of the PostgreSQL server. Let’s query with the following command

        SELECT name, setting, short_desc FROM pg_settings WHERE name = 'wal_level';

4. In this practice exercise, suppose you wanted to change the name of the `aircrafts_data` to `aircraft_fleet`.

        UPDATE pg_tables SET tablename = 'aircraft_fleet' WHERE tablename = 'aircrafts_data';
        ALTER TABLE aircrafts_data RENAME TO aircraft_fleet;


# 3. Transaction logs for recovery

# 4. Backup and restore

1. to backup: 

        pg_dump --username=<your_user> --host=localhost <your_database> > /var/lib/postgresql/data/your_backup_file.sql
        pg_dump -U your_username -h your_host -p your_port -d your_database --no-blobs -F c -v -f your_backup_file.dump

2. to restore:

        createdb -U your_username -h your_host -p your_port new_database_name
        pg_restore -U your_username -h your_host -p your_port -d new_database_name -v your_backup_file.dump
        psql -U your_username -h your_host -p your_port -d new_database_name -f your_backup_file.sql

# 5. Deploy Amazon EC2

To connect to an Amazon EC2 instance using SSH, follow these steps:

Prerequisites:
- Ensure you have the .pem key pair file (private key) that you specified when launching the instance.
- Confirm that your EC2 instance is running and that you have its public DNS name or IP address.
- Verify that your security group allows inbound SSH traffic (port 22).

Steps to Connect (For Linux/macOS)

1. Open a terminal.

2. Set the permissions for your .pem file: `chmod 400 /path/to/your-key-pair.pem`

3. Connect to your instance using SSH: `ssh -i /path/to/your-key-pair.pem ec2-user@your-instance-public-dns`

Replace /path/to/your-key-pair.pem with the path to your .pem file, and your-instance-public-dns with the public DNS name or IP address of your EC2 instance. The default username is ec2-user for Amazon Linux, but it can vary depending on the AMI:
- Amazon Linux, CentOS, RHEL: `ec2-user`
- Ubuntu: `ubuntu`
- Debian: `admin` or `root`
- SUSE: `ec2-user` or `root`

3. install postgres follow this page:

- To install PostgreSQL, first refresh your server’s local package index: `sudo apt update`

- Then, install the Postgres package along with a -contrib package that adds some additional utilities and functionality: `sudo apt install postgresql postgresql-contrib`

- Check the installation `sudo systemctl status postgresql`

- The installation procedure created a user account called postgres that is associated with the default Postgres role. There are a few ways to utilize this account to access Postgres. One way is to switch over to the postgres account on your server by running the following command: `sudo -i -u postgres`

- Then you can access the Postgres prompt by running: `psql`

4. modify the file to accept connection from anywhere

- Backup `postgresql.conf` config file: `sudo cp /etc/postgresql/14/main/postgresql.conf /etc/postgresql/14/main/postgresql.conf.bak`

- Open text editor: `sudo nano /etc/postgresql/14/main/postgresql.conf`

- Edit `postgresql.conf` to listen on all IP addresses:

        sudo nano /var/lib/pgsql/data/postgresql.conf  # Amazon Linux
        sudo nano /etc/postgresql/13/main/postgresql.conf  # Ubuntu

Find the line listen_addresses and set it to:

        listen_addresses = '*'


- Change the password of postgres user: `sudo passwd postgres`

- Login using postgres system account: `su - postgres`

- Change the database postgres password `psql -c "ALTER USER postgres WITH PASSWORD '<your_password>'"`

- Backup `pg_hba.conf` config file: `sudo cp /etc/postgresql/14/main/pg_hba.conf /etc/postgresql/14/main/pg_hba.conf.bak`

- modify the following file to allow remote connections: `sudo nano /etc/postgresql/14/main/pg_hba.conf`

- change the content: 

        # IPv4 local connections:
        host    all             all             127.0.0.1/32            scram-sha-256

        to

        # IPv4 local connections:
        host    all             all             0.0.0.1/0            md5

- restart postgresql `sudo systemctl restart postgresql`