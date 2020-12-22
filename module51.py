################## METADATA ##################
# NAME: Roberto Canovas
##############################################


import systemd.login 
import pwd
import subprocess
#Importerar de bibliotek som behövs för att kunna hämta information om användare, processer, paths etc.

def listusers(): #skapar funktionen listusers
    lista = [] #skapar en lista för att senare kopiera innehållet till listan
    ordBok = {} #skapar en dictionary
    for users in pwd.getpwall(): # för varje användare i funktionen pwd.getpwall, detta funktion hämtar infro från passwd filen
        ordBok["användare"] = ("{0: <20}").format(users.pw_name) #här läggs användare in i dictionary och sedan formaterar denna kolumn
        ordBok["Shell"] = ("{0: <10}").format(users.pw_shell) #Här hämtas informationen om shell och formaterar även denna kolumn
        ordBok["UID"] = ("{0: <5}").format(users.pw_uid) #Här hämtas informationen om uid och formaterar kolumnen.

        inloggade = systemd.login.uids() #variabeln inloggade skapas för att tillkall den istället för funktionen systemd.login.uids
        for användare in inloggade:
            if användare == users.pw_uid:
                ordBok["inloggade"] = True
            else:
                ordBok["inloggade"] = False
                #Här skapas en if-sats för att sätta true eller false beroende på om användaren är inloggad eller inte.
        lista.append(ordBok.copy()) #Här kopieras allt från ordboken till listan för att sedan lista outputen.
    lista.sort(key=lambda x : int(x["UID"])) #Sortering sker på uid, dock så görs uid om till en integer för att sorteringen ska kunna ske

    return(lista)


def diskusagehome(uid): #definierar en funktion vid namn diskusagehome

    try : 
        path = pwd.getpwuid(uid).pw_dir #Använder funktionen pwd.getpwuid för att få ut hemkatalogen för de aktuella uid.
        #Try testar om den får ut det aktuella värdet, ett exempel är att systemanvändare inte har en hemkatalog vilket kommer skickas ned till except.
    except KeyError : #här samlas alla errors som kan fås ut när den testar den aktuella koden ovanför
        return None 
    disk = subprocess.check_output(['sudo','du','-s','-m',path]).decode('utf-8').split('\t')[0] #Här hämtas informationen med hjälp av linux kommandot du.
        #du står för diskusage och detta körs med sudo för att vara säker på att åtkomst accepteras. -s -m är flaggor för att få ut rätt information, där -m står för Megabyte
        # -s visar innehållet för alla filer och mappar.
    disk = int(disk) #Här tilldelas variablen disk datatypen integer för att kunna få ut rätt output.
    return disk

    