from fabric.api import *

#env.users='localuser'

env.hosts=['localuser@studvm16-p.cs.ucl.ac.uk']


def deploy():
	run("git clone https://github.com/ironbila/Scenario1")
    sudo("systemctl stop httpd")
    sudo("cp Scenario1/project-dir/. /var/www/html/ -R")
    sudo("cp Scenario1/utils/finalconfig.conf /etc/httpd/conf.d/ -R")
    sudo("usermod -a -G localuser apache")
    sudo("chmod 710 /home/localuser")
    sudo("chmod 664 /var/www/html/project-dir/backend/todolist/db.sqlite3")
    sudo("chown apache /var/www/html/project-dir/backend/todolist/db.sqlite3")
    sudo("chown apache /var/www/html/project-dir/backend/todolist")
    sudo("systemctl start httpd")
    sudo("sudo rm -rf Scenario1")

def environment_set_up():
    sudo("yum install epel-release")
    sudo("yum install python-pip")
    sudo("cpip install -U setuptools")
    sudo("pip install Django")
    sudo("systemctl start httpd")
    sudo("yum install python-setuptools http mod_wsgi")

def clean():
    sudo("systemctl stop httpd")
    sudo("rm -rf /var/www/html/")
    sudo("rm -rf /etc/httpd/conf.d/finalconfig.conf")


