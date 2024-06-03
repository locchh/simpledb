# Install docker

1. Run the following command to uninstall all conflicting packages:

        for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

2. Set up Docker's apt repository.

        # Add Docker's official GPG key:
        sudo apt-get update
        sudo apt-get install ca-certificates curl
        sudo install -m 0755 -d /etc/apt/keyrings
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
        sudo chmod a+r /etc/apt/keyrings/docker.asc

        # Add the repository to Apt sources:
        echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update


3. Install the Docker packages.

        sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

4. Verify that the Docker Engine installation is successful by running the hello-world image.

        sudo docker run hello-world

# Install UI

# Install pgadmin

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

# Install phpmyAdmin

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
