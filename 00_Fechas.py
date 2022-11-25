# Fechas

from datetime import datetime


now = datetime.now()
print (now) # Nos dice fecha y hora
print (now.hour) # Nos dice la hora actual
print (now.year) # Nos dice el año
print (now.month) # Nos dice el mes
print (now.minute) # Nos dice el minuto actual
print (now.second) # Nos dice los segundos actuales
timestamp = now.timestamp()
print (timestamp) # Nos dice el tiempo de una manera peculiar
year_2023 = datetime(2023, 1, 1) # Creamos una fecha nosotros mismos
print (year_2023)

def print_date(date):
    now = datetime.now()
    print(now)  # Nos dice fecha y hora
    print(now.hour)  # Nos dice la hora actual
    print(now.year)  # Nos dice el año
    print(now.month)  # Nos dice el mes
    print(now.minute)  # Nos dice el minuto actual
    print(now.second)  # Nos dice los segundos actuales
    print(year_2023)


print_date(2022)

from datetime import time

current_time = time(21, 6, 0)
print (current_time.hour)
print (current_time.minute)
print (current_time.second)

from datetime import date

current_date = date(2022, 11, 25)
print (current_date.today())
print (current_date.year)
print (current_date.month)

from datetime import timedelta
start_timedelta = timedelta(200, 100, 100,weeks = 10)
end_timedelta = timedelta(300, 100, 100,weeks = 13)  # Timedelta nos muestra la diferencia entre dos fechas u horas
print (end_timedelta - start_timedelta)









