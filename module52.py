################## METADATA ##################
# NAME: Roberto Canovas
##############################################


import systemd.journal
from systemd import journal
import datetime
import socket



def recentlogmessages(systemdunit, priority=journal.LOG_WARNING):    #definierar funktionen recentlogmessages.
   loggs = journal.Reader() #Är ett sätt att läsa loggarna på
   loggs.this_boot() #läser in journals från boot bara.
   loggs.log_level(priority) #hämtar prioriteten som är satt till warning eller info. I uppgiftsbeskrivningen ska den vara warning.
   loggs.add_match(_SYSTEMD_UNIT=systemdunit) #Letar efter systemdunit och läser loggarna från dem.
   for entry in loggs: #en for-loop som itererar i loggs                             
        tidenärinne = entry['_SOURCE_REALTIME_TIMESTAMP'] - datetime.timedelta() #variablen tidenärinne är lika med entry
        if tidenärinne: #en if-sats som printar ut meddelanden i entry
            return entry['MESSAGE'] #Här retuneras varje meddelande till det skript som kallar det, i detta fall testskriptet


def probetcpport(address, portnumber): #definierar en funktion vid namn probetcpport
   
    try: #testar om det finns några errors
        socket.create_connection((address, portnumber), timeout=2) #testar funktionen och om det tar länge än 10sek stängs den ned
    except: #hanterar errors i detta fall att porten och addressen inte stämmer  
        print("probing", address,"on port",portnumber,":failed") #printar ut felmeddelande
    else: # men om det inte finns några errors kommer den skriva ut success
        print("probing", address,"on port ",portnumber,":success") #printar ut success
        
