#!/bin/bash

# cloning the git hub repository
git clone https://github.com/ironbila/django-rep


# stop apache server
sudo systemctl stop httpd


# start deploying
# copy web app content in the html folder
sudo cp django-rep/project-dir/. /var/www/html/ -R

# copy .conf file to apache - needs editing
sudo cp django-rep/utils/finalconfig.conf /etc/httpd/conf.d/ -R

# start server
sudo systemctl start httpd

# delete the repo
sudo rm -rf django-rep



