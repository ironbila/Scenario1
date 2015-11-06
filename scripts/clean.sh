#!/bin/bash

sudo systemctl stop httpd

sudo rm -rf /var/www/html/

sudo rm -rf /etc/httpd/conf.d/finalconfig.conf

