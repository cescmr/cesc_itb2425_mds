"""
Javier Amaya Boira
02/10/2023
ASIXc M03 UF1 A2
Exemple de manipulació de dates
https://www.w3schools.com/python/python_datetime.asp
"""
import datetime

avui = datetime.datetime.now()

print(avui)

print(avui.year)

print(avui.strftime("%A")) # strftime() method, to create a formatted string

dataNaixement = datetime.datetime(2005, 2, 28)  # dia 29 o dia 30 o dia 31 ??

print(dataNaixement)

print("El dia que vas néixer era: " + dataNaixement.strftime("%A"))