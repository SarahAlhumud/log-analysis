#!/usr/bin/python3

import psycopg2


db = psycopg2.connect("dbname=news")
c = db.cursor()

# Create View to join log table with author table
createView = "CREATE OR REPLACE VIEW logArticlesView AS " \
            "SELECT a.title, COUNT(l.path) AS views, a.author " \
            "FROM log AS l, articles AS a " \
            "WHERE substr(l.path, 10) = a.slug " \
            "GROUP BY a.author, a.title;"

c.execute(createView)
db.commit()


firstQuery = "SELECT * " \
            "FROM logArticlesView " \
            "ORDER BY views DESC " \
            "LIMIT 3;"

c.execute(firstQuery)
firstQueryRows = c.fetchall()

print("What are the most popular three articles of all time?")

for row in firstQueryRows:
    print("\"", row[0], "\"", " -- ", row[1], " views", sep='')


secondQuery = "SELECT a.name, SUM(v.views) " \
              "FROM authors AS a, logArticlesView AS v " \
              "WHERE a.id = v.author " \
              "GROUP BY a.name " \
              "ORDER BY SUM(v.views) DESC;"

c.execute(secondQuery)
secondQueryRows = c.fetchall()

print("\nWho are the most popular article authors of all time?")

for row in secondQueryRows:
    print(row[0], " -- ", row[1], " views", sep='')


thirdQuery = "SELECT q1.date , round((CAST(q2.errors AS decimal)/q1.totals) * 100, 2) AS result " \
             "FROM (SELECT to_char(l1.time, 'Mon DD,YYYY') AS date , COUNT(l1.status) AS totals " \
                    "FROM log AS l1 " \
                    "GROUP BY date " \
                    "ORDER BY date) AS q1, " \
                    "(SELECT to_char(l1.time, 'Mon DD,YYYY') AS date , COUNT(l1.status) AS errors " \
                    "FROM log AS l1 " \
                    "WHERE l1.status != '200 OK' " \
                    "GROUP BY date " \
                    "ORDER BY date) AS q2 " \
             "WHERE q1.date = q2.date AND round((CAST(q2.errors AS decimal)/q1.totals)*100, 2) > 1.00 ;"

c.execute(thirdQuery)
thirdQueryRows = c.fetchall()

print("\nOn which days did more than 1% of requests lead to errors?")

for row in thirdQueryRows:
    print(row[0], " -- ", row[1], "% errors", sep='')
