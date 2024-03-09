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

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
