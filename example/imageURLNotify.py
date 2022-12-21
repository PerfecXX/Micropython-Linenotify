# Import Library
from network import WLAN,STA_IF
from linenotify import LineNotify

# Network Credential
ssid = '<YOUR_NETWORK_SSID>'
password = '<YOUR_NETWORK_PASSWORD>'

# Network Interface 
wlan = WLAN(STA_IF)
wlan.active(True)

# Start Connection
print('Connecting...')
wlan.connect(ssid,password)
while not wlan.isconnected():
    pass

# Connection Config
print(wlan.ifconfig())

# Create your line profile  
line = LineNotify('YOUR_LINE_NOTIFY_TOKEN')

# Notify image from URL with text message
# line.notifyImageURL('<Image URL>','<Message>')
line.notifyImageURL('https://static.wikia.nocookie.net/chainsaw-man/images/1/1b/Pochita.PNG','Pochita')

