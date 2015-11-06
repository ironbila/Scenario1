#!/bin/bash

directory='/var/www/html/project-dir/backend/todolist'
backupfile="dbbackup-$(date "+%Y%m%d%H%M").bak"

echo "storing backup database in" $backupfile

ssh localuser@studvm53-p "cd $directory && sqlite3 db.sqlite3 .dump > $backupfile && scp $backupfile localuser@studvm16-p:Documents/backup && rm $backupfile"
