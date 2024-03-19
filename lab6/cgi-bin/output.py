#!/usr/bin/env python3
import cgi
import html
import sqlite3
import os
import cgi
import html

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>You</title>
        </head>
        <body>""")
connection = sqlite3.connect('transport.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()    


cursor.execute("SELECT id_station, station_name FROM bus_station")
data = cursor.fetchall()
print("""<table border="1">
<caption>Автостанции</caption>
  <thead>
    <tr>
      <th>Код пункта</th>
      <th>Пункт</th>
    </tr>
  </thead>
  <tbody>
    """)
for row in data:
    print("<tr>")
    print("<td>{0}</td>".format(row['id_station']))
    print("<td>{0}</td>".format(row['station_name']))
    print("</tr>")
print("""</tbody>
    </table><br>""")


cursor.execute("SELECT * FROM routes")
data = cursor.fetchall()
print("""<table border="1">
<caption>Рейсы</caption>
  <thead>
    <tr>
      <th>Код рейса</th>
      <th>Пункт отправления</th>
      <th>Пункт прибытия</th>
      <th>Время отправления</th>
      <th>Время прибытия</th>
      <th>Стоимость</th>
    </tr>
  </thead>
  <tbody>""")
for row in data:
    print("<tr>")
    print("<td>{0}</td>".format(row[0]))
    print("<td>{0}</td>".format(row[1]))
    print("<td>{0}</td>".format(row[2]))
    print("<td>{0}</td>".format(row[3]))
    print("<td>{0}</td>".format(row[4]))
    print("<td>{0}</td>".format(row[5]))
    print("</tr>")
print("""</tbody>
    </table><br>""")


cursor.execute("SELECT * FROM passenger")
data = cursor.fetchall()
print("""<table border="1">
<caption>Пассажиры</caption>
  <thead>
    <tr>
      <th>id</th>
      <th>ФИО</th>
      <th>Дата рождения</th>
      <th>Паспротные данные</th>
    </tr>
  </thead>
  <tbody>
    """)
for row in data:
    print("<tr>")
    print("<td>{0}</td>".format(row[0]))
    print("<td>{0}</td>".format(row[1]))
    print("<td>{0}</td>".format(row[2]))
    print("<td>{0}</td>".format(row[3]))
    print("</tr>")
print("""</tbody>
    </table><br>""")


cursor.execute("SELECT * FROM pass_routes")
data = cursor.fetchall()
print("""<table border="1">
<caption>Пассажиры и рейсы</caption>
  <thead>
    <tr>
      <th>id пассажира</th>
      <th>Код рейса</th>
    </tr>
  </thead>
  <tbody>
    """)
for row in data:
    print("<tr>")
    print("<td>{0}</td>".format(row[0]))
    print("<td>{0}</td>".format(row[1]))
    print("</tr>")
print("""</tbody>
    </table>""")