# Linux web server configuration

Project based on the Udacity ecouse **Configuration Linux Web Server** (udacity.com)

In the beginning we will use **Vegrant** to configure a ubuntu virtual machine.

    avgrant init ubuntu/trusty64
    vagrant up

**/bin** : where executable binaries ares stored, accesable from all users
**/sbin** : binaries used by only the root user for sysadmin and maintenance. This directory holds all of the applications you may need as an administrator, but normal users typically won't use.
**/lib** : for libs that support binaries that are located around the system.
**/etc** is where configuration files are stored. For example database and server configuration files
**/var** : Files that can change in size (grow) over time. System and application logs are stored in
this directory.
**/usr** : is for user's programs.

**PATH** : is where linux check for executable binaries. [Adding](https://help.ubuntu.com/community/EnvironmentVariables) a directory to the path by editing the .bashrc file adding export PATH="/path/to/dir:$PATH". But this works only for programs executed by the bash.

    source ~.bashrc


- Package source list : a list of items from where we can get software

    cat /etc/apt/source.list

- **Finger**: This application will look up varius pieces of information about a user, and display it in an easy to read format.

    finger
    finger $USER

The file from where finger gets all this information is **/etc/passwd** It's used to keep track of all users on the system. The info about the specific user is organized.

    username:password:UID:GID:UID info:home directory:command/shell

Let’s run through what each of those mean:

- username: the user’s login name
- password: the password, will simply be an x if it’s encrypted
- user ID (UID): the user’s ID number in the system. 0 is root, 1-99 are for predefined users, and 100-999 are for other system u nts
- group ID (GID): Primary group ID, stored in /etc/group.
- user ID info: Metadata about the user; phone, email, name, etc.
- home directory: Where the user is sent upon login. Generally /home/
- command/shell: The absolute path of a command or shell (usually /bin/bash). Does not have to be a shell though!


## Dasabling the ssh root access

- Adding a new user

    sudo adduser 
    
- Remotly connecto to a vagrant machine

    ssh hostname@localhost -p 2222

The new user does't have permissions to use the **sudo** command. So to fix it, we will use another user with sudo right that we can check at

    /etc/sudousers 

The last line indicates **#includedir /etc/sudoers.d** this command tells the system to also look in this directory for files and include those as if they were written directly within this file. This is done in the way to save the costom settings inserted by the administrators and avoid loosing this configuration furing system updates.

Giving access to sudo to a new user: 

    sudo cp /etc/sudoers.d/vagrand /etc/sudoers.d/student
    sudo nano /etc/sudoers.d/student


## Authentication process.
We will generate a key pair in our local/client machine and after we will move the .pub in our server (vargrant machine) in the way to enable ssh key authentication.

Generating a key-pair using ssh-kyegen

    ssh-keygen # saved them on ~/.ssh/linuxCourse

The ssh-keygen have generated two files 

- linuxCourse
- linuxCourse.pub

The .pub file is the one that will be placen the server to enable the key based authentication.

On the server machine create a new speacial file

    touch ~/.ssh/authorized_keys 
    
In this file are stored all the public keys this account is allowed to use for authentication. The file structure is one key per line. Now we copy here all the .pub keys. Next we change permissions on .ssh folder and files to ensure other users can't have access to this keys. 

    chmod 700 ~/.ssh # only the owner che r w x on this directory
    chmod 644 ~/.ssh/athorized_keys # only the owner can write on this file

Now we can log in our server using the key instead of the password.

    ssh student@localhost -p 2222 -i ~/.ssh/linuxCorse
 
Disabling the password log in: To do so we need to change the /etc/ssh/sshd_config on the server.Change the value of

    PasswordAuthentication yes/no

Restart the ssh service to enable the new configuration.


## Firewall UFW

        sydo ufw status

Adding rules to the Firewall:
- block all the ports so after we can enable only the ones we really need

        sudo ufw default deny incoming

- allow all the outgoing communications

        sudo ufw default allow outgoing

- open the respectiving ports

        sudo ufw allow ssh
     
        sudo ufw allow 2222/tcp 
     
        sudo ufw allow www

        sudo ufw allow https

        sudo ufw enable

Server configured and ready for installing and testing software


- ["LAMP" Stack (Linux, Apache, MySQL, PHP)](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04)

- ["LEMP" Stack (Linux, nginx, MySQL, PHP)](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-14-04)

- [PEPS Mail and File Storage](https://www.digitalocean.com/community/tutorials/how-to-run-your-own-mail-server-and-file-storage-with-peps-on-ubuntu-14-04)

- [Mail-in-a-Box Email Server](https://www.digitalocean.com/community/tutorials/how-to-run-your-own-mail-server-with-mail-in-a-box-on-ubuntu-14-04)

- [Lita IRC Chat Bot](https://www.digitalocean.com/community/tutorials/how-to-install-the-lita-chat-bot-for-irc-on-ubuntu-14-04)




