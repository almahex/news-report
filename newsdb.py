#!/usr/bin/env python

# Package used in order to connect with out PostgreSQL database.
import psycopg2

DBNAME = "news"
TITLE = "\n   NEWS REPORT"
QONE = "\n\n   1. What are the most popular three articles of all time?\n"
QTWO = "\n   2. Who are the most popular article authors of all time?\n"
QTHREE = "\n   3. On which days did more than 1% of requests lead to errors?\n"


def parse_table(table):
    """ Given the result of a select query (always a two column table in this
    case), this function returns a dictionary with all the information parsed
    correctly. In the dictionary, the key will always be the value of the
    first column and the value will be the value of the second column. """
    result = {}
    for key, value in table:
        result[key] = str(value)
    return result


def print_result(n, data):
    """ This function prints the report correctly depending on the
    question. """
    if n == 1:
        print TITLE+QONE
        it = 1
        for key, value in sorted(data.iteritems(), key=lambda (k, v): (v, k),
                                 reverse=True):
            print '      (%i) "%s": %s views\n' % (it, key, value)
            it += 1
        return
    elif n == 2:
        print QTWO
        it = 1
        for key, value in sorted(data.iteritems(), key=lambda (k, v): (v, k),
                                 reverse=True):
            print '      (%i) %s: %s views\n' % (it, key, value)
            it += 1
        return
    elif n == 3:
        print QTHREE
        for key, value in sorted(data.iteritems(), key=lambda (k, v): (v, k),
                                 reverse=True):
            print '      %s: %s' % (key, value) + '% errors\n'
        return
    else:
        print "Invalid selection"


def compute_result(question, query):
    """ This function opens a connection with the database by using the
    package psycopg2, creates a cursor with that database, executes the query,
    closes the connection and fetches the data. This data is then parsed and
    printed by calling two different functions. """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    result_parsed = parse_table(result)
    print_result(question, result_parsed)
    return


""" Queries that retrieve the proper information in order to answer the report
questions. """
compute_result(1, "SELECT title, result.num from articles, " +
               "(SELECT article_slugs.slug, count(*) as num FROM log, " +
               "(SELECT slug FROM articles) as article_slugs WHERE " +
               "log.path = ('/article/' || slug) GROUP BY " +
               "article_slugs.slug) as result WHERE articles.slug " +
               "= result.slug ORDER BY num desc LIMIT 3;")
compute_result(2, "SELECT final_result.name, sum(final_result.num) " +
               "FROM (SELECT authors.name, author_id.num FROM authors, " +
               "(SELECT articles.author, articles_visits.title, num FROM " +
               "articles, (SELECT title, result.num from articles, (SELECT " +
               "article_slugs.slug, count(*) as num FROM log, (SELECT slug " +
               "FROM articles) as article_slugs WHERE log.path = (" +
               "'/article/' || slug) GROUP BY article_slugs.slug) as result " +
               "WHERE articles.slug = result.slug) as articles_visits WHERE " +
               "articles.title = articles_visits.title) as author_id WHERE " +
               "authors.id = author_id.author) as final_result GROUP BY " +
               "final_result.name ORDER BY sum desc;")
compute_result(3, "SELECT result.time::timestamp::date, result.errors FROM " +
               "(SELECT total.time::timestamp::date, trunc((total_error." +
               "count*100)/total.count::decimal, 2) as errors FROM (SELECT" +
               " time::timestamp::date, count(log.status) FROM log GROUP BY" +
               " time::timestamp::date) AS total, (SELECT time::timestamp::" +
               "date, count(log.status) FROM log WHERE status='404 NOT " +
               "FOUND' GROUP BY time::timestamp::date) AS total_error " +
               "WHERE total.time::timestamp::date = total_error.time::times" +
               "tamp::date) as result WHERE result.errors > 1.00;")
