import sqlite3
connection = sqlite3.connect('transport.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE bus_station
            	(id_station INTEGER PRIMARY KEY AUTOINCREMENT, station_name TEXT)''')
cursor.execute('''CREATE TABLE routes
            	(id_routes INTEGER PRIMARY KEY AUTOINCREMENT, departure TEXT, arrival TEXT,
            	departure_time TEXT, arrival_time TEXT,
            	price REAL, foreign key (departure) references bus_station(station_name),
            	foreign key (arrival) references bus_station(station_name))''')
cursor.execute('''CREATE TABLE passenger
            	(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date_of_birth TEXT)''')
cursor.execute('''CREATE TABLE pass_routes
            	(pass_id integer, routes_id integer,
            	foreign key (pass_id) references passenger(id),
            	foreign key (routes_id) references routes(id_routes))''')
cursor.execute("INSERT INTO bus_station (station_name) VALUES ('Краснодар-1')")
cursor.execute("INSERT INTO bus_station (station_name) VALUES ('Краснодар-2')")
cursor.execute("INSERT INTO bus_station (station_name) VALUES ('Адыгейск')")
cursor.execute("INSERT INTO bus_station (station_name) VALUES ('Майкоп')")
cursor.execute("INSERT INTO bus_station (station_name) VALUES ('Анапа')")
cursor.execute("INSERT INTO bus_station (station_name) VALUES ('Энем')")
cursor.execute("INSERT INTO bus_station (station_name) VALUES ('Каменномостский')")
cursor.execute("INSERT INTO routes (departure,arrival,departure_time,arrival_time,price) VALUES ('Краснодар-1', 'Майкоп',"
               "'2024-03-09 13:19', '2024-03-09 15:59', 659.34)")
cursor.execute("INSERT INTO routes (departure,arrival,departure_time,arrival_time,price) VALUES ('Краснодар-1', 'Анапа',"
               "'2024-03-09 9:00', '2024-03-09 13:59', 1019.26)")
cursor.execute("INSERT INTO routes (departure,arrival,departure_time,arrival_time,price) VALUES ('Краснодар-1', 'Каменномостский',"
               "'2024-03-10 6:30', '2024-03-10 12:00', 734.26)")
cursor.execute("INSERT INTO routes (departure,arrival,departure_time,arrival_time,price) VALUES ('Краснодар-2', 'Энем',"
               "'2024-04-12 18:30', '2024-04-12 20:00', 403.54)")
cursor.execute("INSERT INTO passenger(name,date_of_birth) VALUES ('Иванова Екатерина', '1998-12-03')")
cursor.execute("INSERT INTO passenger(name,date_of_birth) VALUES ('Петров Вячеслав', '1963-07-19')")
cursor.execute("INSERT INTO passenger(name,date_of_birth) VALUES ('Крапов Алексей', '2001-11-06')")
cursor.execute("INSERT INTO pass_routes(pass_id,routes_id) VALUES (1,3)")
cursor.execute("INSERT INTO pass_routes(pass_id,routes_id) VALUES (1,4)")
cursor.execute("INSERT INTO pass_routes(pass_id,routes_id) VALUES (3,2)")
cursor.execute("INSERT INTO pass_routes(pass_id,routes_id) VALUES (2,4)")
# Сохраняем изменения и закрываем соединение
connection.commit()

connection.close()
