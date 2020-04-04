# Stack Web application 

## [Initial Server Setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04)

## ["LAMP" Stack (Linux, Apache, MySQL, PHP)](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04)

A “LAMP” stack is a group of open source software that is typically installed together to enable a server to host dynamic websites and web apps. This term is actually an acronym which represents the Linux operating system, with the Apache web server. The site data is stored in a MySQL database, and dynamic content is processed by PHP.

### 1. Install Apache
The Apache web server is currently the most popular web server in the world

    sudo apt-get update

    sudo apt-get install apache2

    ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'
    
    # the easy way to get the external ip is
    curl ifconfig.me

    lynx localhost

    lynx http://IP_address


### 2. Install MyQql
Now that we have our web server up and running, it is time to install MySQL. MySQL is a database management system. Basically, it will organize and provide access to databases where our site can store information.

    sudo apt-get install mysql-server php5-mysql

    sudo mysql_install_db

    sudo mysql_secure_installation

    sudo mysql_install_db

    service mysql status

    sudo systemctl start mysql

    # launch at boot
    sudo systemctl enable mysql

    /usr/bin/mysql -u root -p

    # allow remote access
    sudo ufw allow mysql


### 3. Install PHP
PHP is the component of our setup that will process code to display dynamic content. It can run scripts, connect to our MySQL databases to get information, and hand the processed content over to our web server to display.


    sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt

Changing Apache settings in the way to serve first the index.php file

    sudo nano /etc/apache2/mods-enabled/dir.conf

    sudo service apache2 restart


### 4. Testing
The root directory where the web pages are seved is /var/www/html/ . Lest create php file.

    sudo nano /var/www/html/info.php

    lynx localhost/php

    # for security reasons is good practice to remove this file
    sudo rm /var/www/html/info.php



- ["LEMP" Stack (Linux, nginx, MySQL, PHP)](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-14-04)

- [PEPS Mail and File Storage](https://www.digitalocean.com/community/tutorials/how-to-run-your-own-mail-server-and-file-storage-with-peps-on-ubuntu-14-04)

- [Mail-in-a-Box Email Server](https://www.digitalocean.com/community/tutorials/how-to-run-your-own-mail-server-with-mail-in-a-box-on-ubuntu-14-04)

- [Lita IRC Chat Bot](https://www.digitalocean.com/community/tutorials/how-to-install-the-lita-chat-bot-for-irc-on-ubuntu-14-04)


# TO DO : Publish to [google Cloud](https://www.christitus.com/wordpress-google-cloud-platform/)
# Free web hosting
