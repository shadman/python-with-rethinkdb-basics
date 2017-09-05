# Python 3.5 with ReThinkDB basics

# Setting up Python

$ sudo apt-get update

$ sudo apt-get -y upgrade

## To verify Python3 version

$ python3 -V

## To manage all python 3 packages, you need to install pip for python 3

$ sudo apt-get install -y python3-pip


## Install pip for Python packages

REF: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-16-04-server

$ sudo apt-get install -y python3-pip

or (for older version)

REF: https://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/

$ sudo apt-get install python-pip python-dev build-essential

$ sudo pip install --upgrade pip

$ sudo pip install --upgrade virtualenv

### After above; you may install your Python 3 packages via 

$ sudo pip3 install <package_name>

or (for older versions)

$ sudo pip install rethinkdb (for older versions)



# Setting up ReThinkDB

REF: https://www.rosehosting.com/blog/install-rethinkdb-on-ubuntu-14-04/

$ source /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list

$ wget -qO- http://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -

$ sudo apt-get update

$ sudo apt-get install rethinkdb

## Start database server on background by:

$ rethinkdb --bind all &

## After executing server may access via:

http://localhost:8080


### NOTE: ReThinkDB port will be 28015


# Setting up database with Python

### Install rethinkdb package for python

$ sudo pip3 install rethinkdb

or (for older versions)

$ sudo pip install rethinkdb 


### For python 3.5 or greater use below commands to install pip (if not installed and having problem with python3 packages)

$ curl -O https://bootstrap.pypa.io/get-pip.py

$ sudo python3.5 get-pip.py



# Use database with Python

## Using RethinkDB with Python

REF: https://www.rethinkdb.com/docs/guide/python/

### Insert
import rethinkdb as r

r.connect('localhost', 28015).repl()
r.db('test').table_create('tv_shows').run()
r.table('tv_shows').insert({ 'name': 'Star Trek TNG' }).run()

### Retrieve 
cursor = r.table("tv_shows").run()
for doc in cursor:
...  print(doc)

### Apply Filter
cursor = r.table("tv_shows").filter(r.row["name"] == "ShanTest").run()
for document in cursor:
    print(document)

### Apply Conditions
cursor = r.table("tv_shows").filter(r.row["posts"].count() > 2).run()
for document in cursor:
    print(document)

### Retrieve Specific Record
r.db('test').table('tv_shows').get('7644aaf2-9928-4231-aa68-4e65e31bf219').run()

