# install UI

# install pgadmin

1. Start by updating your system packages. Ensure your system is up-to-date using the following commands:

        sudo apt-get update
        sudo apt-get upgrade

2. Install the public key for the PgAdmin4 repository:

        curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add

4. Create the repository configuration file:

        sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/focal/ pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

5. Choose your preferred mode for PgAdmin4 installation:

        sudo apt install pgadmin4 (For both desktop and web modes)
        sudo apt install pgadmin4-desktop (For desktop mode only)
        sudo apt install pgadmin4-web (For web mode only)

# install phpmyAdmin

1. Update:

        sudo apt update

2. Install phpMyadmin

        sudo apt install phpmyadmin php-mbstring php-zip php-gd php-json php-curl


- `php-mbstring`: A module for managing non-ASCII strings and convert strings to different encodings
- `php-zip`: This extension supports uploading .zip files to phpMyAdmin
- `php-gd`: Enables support for the GD Graphics Library
- `php-json`: Provides PHP with support for JSON serialization
- `php-curl`: Allows PHP to interact with different kinds of servers using different protocols

3. access phpmyadmin:

        https://your_domain_or_IP/phpmyadmin


