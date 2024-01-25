import calendar

# Solicitar al usuario el año y el número de mes
year = int(input("Ingrese el año: "))
month = int(input("Ingrese el número de mes (1-12): "))

# Crear un objeto de calendario
cal = calendar.month(year, month)

# Imprimir el calendario
print("Calendario para {} {}".format(calendar.month_name[month], year))
print(cal)
