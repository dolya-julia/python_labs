import csv
from datetime import datetime


def num(name):
    months = {'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8,
              'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}
    return months[name]


date2 = datetime.strptime('2017-04-05', '%Y-%m-%d')
num_basic_law = 0
num_economic = 0
with open('3 - 1.csv', encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Фамилия"] != "Среднее по группе" and row["Фамилия"] != "Общее среднее":
            date = row["Тест начат"].split()[:-1]
            test_date = "{}-{}-{}".format(date[2], num(date[1]), date[0])
            date1 = datetime.strptime(test_date, '%Y-%m-%d')
            if date1 > date2:
                if row['В. 1 /1,00'] == '0,00':
                    num_basic_law += 1
                if row['В. 2 /1,00'] == '0,00':
                    num_basic_law += 1
                if row['В. 3 /1,00'] == '0,00':
                    num_economic += 1

print(num_basic_law, num_economic)