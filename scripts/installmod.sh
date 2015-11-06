#!/bin/bash

git clone https://github.com/ironbila/Scenario1

cd django-rep/utils/

tar -xvf mod_wsgi-4.4.21.tar.gz

cd mod_wsgi-4.4.21/

./configure

sudo make install

make clean

cd ..

cd ..

cd ..

sudo rm -rf django-rep
