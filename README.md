# News Report

This application gives insights about a newspaper site.

The database of this newspaper it's called **news** and it has three tables:
* Articles: Provides information about the articles published on the site.
* Authors: Lists all the authors that have written these articles and a small bio from them.
* Log: Includes a log for every time a user has accessed the site.

The report that is generated upon running this app gives answers to the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular authors of all time?
3. On which days did more than 1% of requests lead to erros?

## Usage

### Setting up the environment

The usage of this report is intended to be done by using Vagrant and VirtualBox. Therefore, both of them need to be installed.

Once you have both of them installed in your computer. Download the VM configuration by froking and then cloning this [repo](https://github.com/udacity/fullstack-nanodegree-vm).

Then, `cd` into the **vagrant** directory and paste the file `newsdb.py` here. After this, run `vagrant up` to download the Linux OS and install it.

After this, you just need to do `vagrant ssh` to log in into the VM.

### Running the report

In order to see the report, go to the **news** directory and run the following commands:
* Run `psql -d news -f newsdata.sql` in order to load all the data from the news database
* Run `python newsdb.py` to display the report on you terminal

## Credits

### Resources

* [PostgreSQL Documentation - String Functions and Operators](
https://www.postgresql.org/docs/9.5/functions-string.html)
* [How to sort a Python dict by keys or values](https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/)
* [Data Structures in Python](https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/)
* [PostgreSQL Documentation - Aggregate Functions](https://www.postgresql.org/docs/9.6/functions-aggregate.html)
* [Stack overflow - Extract date from timestamp in PostgreSQL](https://stackoverflow.com/questions/6133107/extract-date-yyyy-mm-dd-from-a-timestamp-in-postgresql)
* [Stack overflow - PostgreSQL query division](https://stackoverflow.com/questions/37249764/divison-with-more-than-one-result-from-postgresql-query)
* [PostgreSQL Documentration - Mathematical Functions and Operators](https://www.postgresql.org/docs/8.1/functions-math.html)

### Contributors

* Sara Garci <rsaragarci@gmail.com>

## License

© Copyright 2018 by Sara Garci. All rights reserved.
