# DONE
* fix non-utf-8 problem
* add list of topics as parameter

# TODO
* csv files not db
* new run = new session
* mqtt logger msg as json not plain text
* provide to text file cfg params: broker, path, start datetime, amount of files in folder, newest db file name
* automate build for all platforms using buildx
* add tag latest
* add one extra test parameter
* add datetime at every ">>>"

# Rejected
* add special meta-command to restart app and create new .db file - nope, another service will do it    



# 2025
* csv
* variables:
  * broker (addr or ip)
  * port
  * username and password
  * clientid ???
* topics???
* .env file
* logs with tags to file
* each run one session
* cicd docker hub
* docker compose sample
* docker cli sample