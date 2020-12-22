################## METADATA ##################
# NAME: Roberto Canovas
##############################################

import re

def aggregatelog(filename):
	ordBok = {}
	IPaddress = {}
	Method = {}
	Path = {}
	Month = {}

#Importerar modulen re och sedan skapas en funktion vid namn aggregatelog.
#Rad 12-16  skapas fem dictionarys, dessa dictionarys kommer sedan att innehålla värderna från den angivna textfilen.
#Dessa dictionarys kommer vara nestad med OrdBok.

	with open(filename, "r") as fil:
		for line in fil.readlines():
			ippattern="^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
			m=re.search(ippattern,line)
			if m:
				IPaddress[m.group(0)]=IPaddress.setdefault(m.group(), 0)+1

			monthpattern="Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
			m=re.search(monthpattern,line)
			if m:
				Month[m.group(0)]=Month.setdefault(m.group(0), 0)+1
			methodpathpattern="(GET|POST|HEAD|PUT|OPTIONS|CONNECT|DELETE|TRACE|PATCH|PROPFIND) ([^ ]*?) HTTP"
			m=re.search(methodpathpattern,line)
			if m:
				Method[m.group(1)]=Method.setdefault(m.group(1), 0)+1 
				Path[m.group(2)]=Path.setdefault(m.group(2), 0)+1

#Här öppnas den angivna filen, riktigta filen finns i testskriptet och därför när denna modul tillkallas kommer filen att köras.
#Filen i detta fall är access.log-2. den första variabeln ippatern är tilldelad en regex sträng som kommer söka efter alla ipadresser.
#Dessa IP-adresser är mellan range 1.1.1.1-999.999.999. Variablen m blir tilldelad funktionen re.search(ippattern,line).
#Detta göra att den söker varje rad i textfilen med regex-strängen för ippattern.
#En if-statement har skapats för att så om variabeln m läggs den gilitiga ip-adressen i försa gruppen.

#Detsamma gäller med variablen monthpattern som blir tilldelad en sträng för att söka efter gilitiga månader. 
#Den sista variabeln methodpathpattern kommer söka efter olika HTTP-metoder, jag har valt att ta med de vanligaste metoderna. 
#Det ([^ ]*?) HTTP regex strängen gör att få fram alla gilitga path efter HTTP.
  
	ordBok["IP"] = IPaddress.copy()
	ordBok["MONTH"] = Month.copy()
	ordBok["METHOD"] = Method.copy()
	ordBok["PATH"] = Path.copy()
	return ordBok


#I de sista raderna kopieras all data in i de olika dictionarys, det är den datan som har sorterats tidigare med hjälp av olika regulara uttryck.
#Nested dictionaryn är nu fylld med data eller keyvalues.
#return ordBok är självbeskrivande och reunerar ut nestade dictionaryn OrdBok.
