#!/bin/bash

# cloning the git hub repository
git clone https://github.com/ironbila/Scenario1


# stop apache server
sudo systemctl stop httpd


# start deploying
# copy web app content in the html folder
sudo cp Scenario1/project-dir/. /var/www/html/ -R

# copy .conf file to apache 
sudo cp Scenario1/utils/finalconfig.conf /etc/httpd/conf.d/ -R

# solve permission issues
sudo usermod -a -G localuser apache
sudo chmod 710 /home/localuser
sudo chmod 664 /var/www/html/project-dir/backend/todolist/db.sqlite3
sudo chown apache /var/www/html/project-dir/backend/todolist/db.sqlite3
sudo chown apache /var/www/html/project-dir/backend/todolist

# start server
sudo systemctl start httpd

# delete the repo
sudo rm -rf Scenario1



