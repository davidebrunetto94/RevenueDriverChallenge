# Code challenge - Back end - RevenueDriver
This script creates a MySQL database using data from a ".csv" file, using Python, the PyMySQL package and Pandas.

## How to run:
To run this project you need:
* Python version >= 3.0. If you don't have it installed on your pc, you can find how to install it [here](https://www.python.org/downloads/)
* MySQL installed. If you don't have it installed on your pc, you can find how to install it [here](https://dev.mysql.com/doc/mysql-getting-started/en/). This project uses the default configuration when connecting to the db, if you used a different one you can change the variables on line 17 of create_db.py;
* Pip, the standard package manager for Python which comes bundled with recent versions of it. You can check if it's installed by opening a command prompt or terminal instance and typing either "pip --version" or "pip3 --version", if the output shows a version number you're good to go.
* Pandas, which you can install by using the command "pip install pandas" or "pip3 install pandas"
* PyMySql, which you can install by using the command "pip install PyMySQL" or "pip3 install PyMySQL"

Once you have installed all the necessary programs and packages, to run simply open a terminal or command prompt in the project directory and type "python .\create_db.py"

## What I would have done differently if I had more time:
Mainly I would have structured the code a little bit better in smaller functions with a clear and single purpose. Since the code isn't that big I think it's still readable and fairly concise but with time (maybe adding more features) it could get a little bit messy.
I would have also searched for a better looking way to parameterize the CREATE TABLE query because I had to resort to the standard format python function, since the mySQL package I'm using doesn't have that possibility by default.
