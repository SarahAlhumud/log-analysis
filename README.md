#Full Stack Web Developer Nano-Degree 
##Project (1): Log Analysis

This is the first project in Full Stack Web Developer Nano-Degree. It shows a report about viewing articles of authors.


`main.py` file is a python file implements three queries:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

It contains a view to help implementing the first two queries:
```
CREATE OR REPLACE VIEW logArticlesView AS
            SELECT a.title, COUNT(l.path) AS views, a.author
            FROM log AS l, articles AS a
            WHERE substr(l.path, 10) = a.slug
            GROUP BY a.author, a.title;
```
            
Since the keyword `REPLACE` will check the existing of the view, no need to omit that query before run code for multiple times.

The output of this code is in `output.txt` file.

### Setup
#####1. Start with Software Installation
  - Vagrant: https://www.vagrantup.com/downloads.html
  - Virtual Machine: https://www.virtualbox.org/wiki/Downloads
  - Download a FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm
and probably you will find the file in your “Download” folder.

\- You will also need a Unix-style terminal program. On Mac or Linux systems, you can use the
built-in Terminal. On Windows, we recommend Git Bash, which is installed with the Git version control software.

Once you get the above software installed, follow the following instructions:
```
cd vagrant
vagrant up
vagrant ssh
cd /vagrant
mkdir log-analysis-pr
```

\- For this project, all the work will be on your Linux machine, so always make sure you logged in by using the following commands:
vagrant up, then vagrant ssh, then cd /vagrant.
Note: Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not.

#####2. Download and Load the Data
  - For this project, you need to download “newsdata.sql” from the project page or by clicking
on the following link:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
  - Move the “newsdata.sql” to your project folder “log-analysis-project”
  - Load the data from the “newsdata.sql” by using the following command: Note that we are
using PostgreSQL for this project:
    ```
    psql -d news -f newsdata.sql
    ```
  - Once you have the data loaded into your database, connect to your database using:
    ```
    psql -d news
    ```
