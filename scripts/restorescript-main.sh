#!/bin/bash

directory='/var/www/html/project-dir/backend/todolist'

cd /home/localuser/Documents/backup/
backupfile=`ls -r dbbackup*.bak | sort -n -t _ -k 2 | tail -1`

echo "restoring database"
scp $backupfile localuser@studvm16-p:$directory
ssh localuser@studvm16-p "cd $directory && mv db.sqlite3 db.sqlite3.old && sqlite3 db.sqlite3 < $backupfile && rm $backupfile"
