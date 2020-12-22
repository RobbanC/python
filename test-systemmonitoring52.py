################## METADATA ##################
# NAME: Roberto Canovas
##############################################


from module-log-cpport52 import recentlogmessages
from module-log-cpport52 import probetcpport


address = ["127.0.0.1", "127.0.0.1", "1.1.1.1", "imap.example.com", "www.example.com", "www.example.com"]
port = ["22", "23", "22", "993", "443", "666"]
#Två stycken listor skapas för att lagra ipadress och tillhörande portar.
for x, y in zip(address, port): 
    probetcpport(x, y)


systemd ="systemd-udevd.service" #tilldelar variablen en tjänst vilket är systemd-udevd.service
ssh = "ssh.service" #tilldelar variabeln en tjänst vilket ssh.service
cron ="cron.service" #tilldelar variabeln en tjänst vilket är cron.service
print(recentlogmessages(systemd)) #skriver ut senaste log meddelandet från systemd 
print(recentlogmessages(ssh)) #skriver ut senaste log meddlenadet från ssh
print(recentlogmessages(cron)) #skriver ut senaste log meddlenadet från cron
