#!/usr/bin/env python3
import cgi
import html
import sqlite3
import os
import cgi
import html
import json
connection = sqlite3.connect('transport.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>python lab</title>
        </head>
        <body>""")

print('<form action="?" method="post">')
print("Выберите таблицу для заполнения:")
tuples_list = [('bus_station', 'Автостанции'), ('routes', 'Рейсы'),('passenger', 'Пассажиры'),('pass_routes', 'Пассажиры и рейсы')]
form = cgi.FieldStorage()
selected_table = form.getfirst("table", "не задано")
print('<select name="table" id="table_select">')
for item in tuples_list:
        if selected_table == item[0]:
                print('<option value={0} selected>{1}</option>'.format(item[0], item[1]))
        else:
                print('<option value={0}>{1}</option>'.format(item[0], item[1]))
print('</select>')

print('<input type="submit" name="go_to" value="Перейти">')
print('<input type="submit" name="save" value="Сохранить">')
print('<input type="submit" name="export" value="Экспорт">')
print('<input type="submit" name="import" value="Импорт">')


selected_button_go = form.getfirst("go_to", "")
selected_button_save = form.getfirst("save", "")
selected_button_export = form.getfirst("export", "")
selected_button_import = form.getfirst("import", "")

if selected_button_go:
        if selected_table == 'bus_station':
                print("""<br>Добавление автостанции:
                <input type="text" name="station_name"><br>
                <br>""")
        elif selected_table == 'routes':
                print("""<br>Добавление рейса:<br>
                Пункт отправления:""")
                cursor.execute("SELECT id_station, station_name FROM bus_station")
                data = cursor.fetchall()
                print("""<select name="routes_departure">""")
                for row in data:
                        print('<option value={0}>{1}</option>'.format(row['id_station'], row['station_name']))
                print("""</select>""")
                print("""<br>Пункт прибытия:
                <select name="routes_arrival">""")
                for row in data:
                        print('<option value={0}>{1}</option>'.format(row['id_station'], row['station_name']))
                print("""</select>""")
                print("""<br>
                Время отправления:
                <input type="text" name="departure_time"><br>
                Время прибытия:
                <input type="text" name="arrival_time"><br>
                Цена:
                <input type="text" name="price"><br>""")
        elif selected_table == 'passenger':
                print("""<br>Добавление пассажира:<br>
                <br>Имя:
                <input type="text" name="pass_name"><br>
                Дата рождения:
                <input type="text" name="date_birth"><br>
                Паспортные данные:
                <input type="text" name="passport"><br>""")
        elif selected_table == 'pass_routes':
                cursor.execute("SELECT id, name FROM passenger")
                data = cursor.fetchall()
                print("""<br>Выберите пассажира:
                <select name="select_pass">""")
                for row in data:
                        print('<option value={0}>{1}</option>'.format(row['id'], row['name']))
                print("""</select>""")
                cursor.execute("SELECT id_routes, departure, arrival FROM routes")
                data = cursor.fetchall()
                print("""<br><br>Выберите рейс:
                <select name="select_route">""")
                for row in data:
                        print('<option value={0}>{1}</option>'.format(row['id_routes'], row['departure'] + '--' + row['arrival']))
                print("""</select>""")
connection.close()
print('</form>')
if selected_button_save:
        connection = sqlite3.connect('transport.db')
        cursor = connection.cursor()
        if selected_table == 'bus_station':
                station_name = form.getfirst("station_name", "")
                station_name = html.escape(station_name)
                cursor.execute("INSERT INTO bus_station (station_name) VALUES (?)",([station_name]))
                connection.commit()

        elif selected_table == 'routes':
                cursor.execute("SELECT id_station, station_name FROM bus_station")
                data = cursor.fetchall()
                id_departure = html.escape(form.getfirst("routes_departure", ""))
                id_arrival = html.escape(form.getfirst("routes_arrival", ""))
                for row in data:
                        if int(row[0]) == int(id_departure):
                                routes_departure = row[1]
                        if int(row[0]) == int(id_arrival):
                                routes_arrival = row[1]
                departure_time = html.escape(form.getfirst("departure_time", ""))
                arrival_time = html.escape(form.getfirst("arrival_time", ""))
                price = html.escape(form.getfirst("price", ""))
                if all((routes_departure, routes_arrival, departure_time, arrival_time, price)):
                        cursor.execute("INSERT INTO routes (departure, arrival, departure_time, arrival_time, price) VALUES (?, ?, ?, ?, ?)",([routes_departure,routes_arrival,departure_time,arrival_time,price]))
                        connection.commit()   
        if selected_table == 'passenger':
                pass_name = html.escape(form.getfirst("pass_name", ""))
                date_birth = html.escape(form.getfirst("date_birth", ""))
                passport = html.escape(form.getfirst("passport", ""))  
                if all((pass_name, date_birth, passport)):
                        cursor.execute("INSERT INTO passenger (name, date_of_birth, passport) VALUES (?, ?, ?)",([pass_name, date_birth, passport]))
                        connection.commit()  
        if selected_table == 'pass_routes':
                pass_id = html.escape(form.getfirst("select_pass", ""))
                routes_id = html.escape(form.getfirst("select_route", ""))
                if all((pass_id , routes_id)):
                        cursor.execute("INSERT INTO pass_routes (pass_id, routes_id) VALUES (?, ?)",([pass_id, routes_id]))
                        connection.commit() 
        print("<p>Данные сохранены!</p>")
        # закрываем соединение с базой данных
        connection.close()                
print("""</body>
        </html>""")

print('<form action="output.py">')
print('<input type="submit" value="Вывод таблиц">')
print("</form><br>")



