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
line = LineNotify('<YOUR_LINE_NOTIFY_TOKEN>')

# Send notify to line with sticker and text 
# line.notifySticker('<Sticker Package ID>','<Sticker ID>','<Message>')
# see more sticker list: https://developers.line.biz/en/docs/messaging-api/sticker-list/
line.notifySticker(3,240,'Nice Sticker')
