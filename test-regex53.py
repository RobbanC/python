################## METADATA ##################
# NAME: Roberto Canovas
##############################################

import module53
values  = module53.aggregatelog('access.log')


#Importerar modulen module53.
#Här skapas en variabel vid namn values, denna blirt tilldelad värdet module53.aggregatelog('access.log-2)
#Detta gör att accesslog filen kommer köras.

mIP = max(values ["IP"], key=lambda k : values["IP"][k])
print("Number of unique IP addresses:", len(values.get("IP")))
print( "Most popular value is: {} : ({} gånger)".format (mIP, values["IP"][mIP]))

#Ovanför kommer variabeln mIP bli tillded maxvärvärdet för IP och denna maxvärden som hittades i modulen kommer hämtas och sedan skrivas ut.
#Här formateras värderna i separata kolumner för att lättare kunna utläsa värderna. len(values.get("IP")) retunerar antalet objekt och hämtar värde i dict "IP"
#lambda används för att definiera en anonym funktion som sedan används
#Variablen mIP lagrar alltså de största värdena som antal gånger och hur många unika IPadresser det finns.

mMetod = max(values ["METHOD"], key=lambda k : values["METHOD"][k])
print("Number of unique HTTP methods:", len(values.get("METHOD")))
print( "Most popular value is: {} : ({} gånger)".format( mMetod, values["METHOD"][mMetod]))

mPath = max(values ["PATH"], key=lambda k : values["PATH"][k])
print("Number of unique paths:", len(values.get("PATH")))
print( "Most popular value is: {} : ({} gånger)".format(mPath, values["PATH"][mPath]))

mMonth = max(values ["MONTH"], key=lambda k : values["MONTH"][k])
print("Number of unique months:", len(values.get("MONTH")))
print( "Most popular value is: {} : ({} gånger)".format (mMonth, values["MONTH"][mMonth]))


#I denna testfil så är alla rader identiska förutom det att nya variabler har skapats för att kunna få ut, 
#maxvärderna för den data som är av intresse. Därför har jag valt att bara kommentera rad 10-12. 
#De värden som hämtas ut är Unika HTTP metoder, populäraste metoden där variabeln mMETOD lagrar och skriver ut max för just det.

#Variabeln mPATH fungerar på precis samma sätt, att lagra, hämta och formatera den aktuella datorn för de antal unika/populäraste 
#värdet av paths.

#mMonth lagrar, hämtar och formaterar alla unika månader, populäraste måndaen och sedan skriver ut de värdet.
