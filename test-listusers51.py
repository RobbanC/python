################## METADATA ##################
# NAME: Roberto Canovas
##############################################



from module51 import listusers, diskusagehome
import pwd
import systemd.login


for info in listusers(): 
        online = ""
        if info["inloggade"] == True:
            online="*"
        else:
            online=" "
#Här skapas en if-sats för att sätta en stjärna på alla inloggade användare i funktionen listusers
        print("{} | {} | {} | {}".format(online, info["UID"], info["användare"], info["Shell"]))
        #Här sker printningen av kolumnen uid, användare och shell, dessa formateras även för en finare output.



uids = [0, 1000, 7777] #variabeln uids tilldelas userid 0,1000,7777
for uid in uids :   #en for loop som itererar genom uids
    value = diskusagehome(uid) #variabeln value är lika med diskusagehome funktionen.
    if value!=None:
        print("Disk usage of user with UID:", uid, ':', value, 'MB')
    else:
        print("Disk usage of user with UID:",uid, ':', "cannot determine")
        #En if-sats skapas för att se om diskanvändningen är mer än 0 eller inte. Det är viktigt för att få ut rätt output.



