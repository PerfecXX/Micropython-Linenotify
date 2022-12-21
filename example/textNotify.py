# Import Library
from network import WLAN,STA_IF
from linenotify import LineNotify

# Network Credential
ssid = '<YOUR_NETWORK_SSID>'
password = '<YOUR_NETWORK_PASSWORD>'

# Network Interface 
wlan = WLAN(STA_IF)
wlan.active(True)

# Start Network Connection
print('Connecting...')
wlan.connect(ssid,password)
while not wlan.isconnected():
    pass

# Network Connection Configuration
print(wlan.ifconfig())

# Create your line profile 
line = LineNotify('<YOUR_LINE_NOTIFY_TOKEN>')
# Send notify to line 
line.notify('สวัสดีครับ')

