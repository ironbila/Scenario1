#!/bin/bash

# setting up the environment

#install epel rep that contains missing packages
sudo yum install epel-release

#install pip
sudo yum install python-pip

#install setuptools
sudo pip install -U setuptools

#install django
sudo pip install Django

#install mod_wsgi
sudo yum install python-setuptools http mod_wsgi