'''
Database
========
Need
-----
To store data permanently in a structured manner, there is
need of database.

data and information
====================

data is called as raw facts  that are recorded.

information is called as processed data.

There are 10000 trains in the database of indian railway.
you searched for trains running between mumbai to delhi.
You got list of 5 trains in front of you.
Out of these 10000 trains you receive 5 trains.

10000 trains available is data .
process: filtering based on source and destination given
         by you.

5  trains running between mumbai and delhi.
5 Trains are called as information.

              filtering process
10000 Trains -----------------> 5 trains between Mumbai to Delhi
Data              process        information

Database : Collection of similar and related records is called
========   as database.

data type: text,images,video,audio etc

              Data      Database
              ==================
              video     Youtube
              Images    Instagram
              audio     spotify/ganna

Database management system [DBMS]
===========================
The system which manages data i.e it helps you to create
database,create tables in database, insert record into
database,delete,update and view all records from database table.

DBMS:oracle,mysql,microsoft sql etc.


xampp: This is a distribution package which constains different
       services, one of them is mysql.


x-cross platform as it works on all operating system.
a-apache [server]
m-mysql  [DBMS]
p-PHP    [PHP interpreter]
p-Pearl  [pearl interpreter]


To download xampp
================
www.apachefriend.com/download



'''
'''
In database, data is stored in the form of table.

By using Mysql DBMS
step1:create database.=> Done
step2:create table inside database to store record.

     tablename:employee
     table employee stores employee information

        id   name  dept  sal
        --------------------
        1    Harry IT    70000
        2    Mac   HR    60000
        3    Shree IT    95000

Number of columns:4

column name    datatype
id             int 
name           varchar(size) => size:number of character    
dept           varchar(size)
sal            float

Table creation done.

                write()
              ------------->
     .py file               data.txt
              <-------------
              read(),readlines()


                                     database

                                     employee
                                     
             insert query        id   name dept sal 
             ------------------->
    .py file                          

             <------------------
               select query

1) insert record from python into database table
2) retrieve all records from database table into python file
3) delete record from database table from python file.
4) update record from database table from python file.

   CRUD
   C=> Create
   R=> Read
   U=> Update
   D=> Delete

'''



















'''
