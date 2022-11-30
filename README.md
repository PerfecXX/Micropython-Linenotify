# MicroPython Line Notify
It is a MicroPython library for sending notifications to Line Notify,which can be used with ESP8266 and ESP32.     
Can send both text messages, stickers and images.

# Prerequisite
- ESP32/ESP8266 with MicroPython installed and can connect to the internet 
- Line Notify Token

# How to get Line Notify Token
Login at https://notify-bot.line.me/en/.
![](https://github.com/PerfecXX/MicroPython_LineNotify/blob/main/doc/image/1_linePage.png?raw=true)
At the top-right dropdown menu, select **my page** .
![](https://github.com/PerfecXX/MicroPython_LineNotify/blob/main/doc/image/3_selectMyPage.png?raw=true)
Scroll down the browser window to find **Generate Token**.
![](https://github.com/PerfecXX/MicroPython_LineNotify/blob/main/doc/image/4_GenerateToken.png?raw=true)
Enter your **Token Name** then select **chat** or **group **.
![](https://github.com/PerfecXX/MicroPython_LineNotify/blob/main/doc/image/5_GenToken.png?raw=true)

Click **Generate Token**, and the token will be generated.
![](https://github.com/PerfecXX/MicroPython_LineNotify/blob/main/doc/image/6_copyToken.png?raw=true)

# Usage 
- Create Instance and set token
```python
line = LineNotify('<token>')
```
- Notify text message
```python
line.notify('<message>')
```
- Notify sticker with text message

Sticker List: https://developers.line.biz/en/docs/messaging-api/sticker-list/ 
```python
line.notifySticker('<Sticker Package ID>','<Sticker ID>','<Message>')
```
- Notify image from URL with text message
```python
line.notifyImageURL('<Image URL>','<Message>')
```

# Example Code
```python
# Import Library
from linenotify import LineNotify
from network import WLAN,STA_IF

# Network Setup
ssid = '<ssid>'
password = '<password>'
wlan = WLAN(STA_IF)
wlan.active(True)
print('Connecting...')
wlan.connect(ssid,password)
while not wlan.isconnected():
    pass
print(wlan.ifconfig())

# Set Line Token 
line = LineNotify('<token>')
# Notify text message 
line.notify('Hello World!')
# Notify sticker with message
line.notifySticker(3,240,'Nice Sticker')
# Notify image from URL with message
line.notifyImageURL('https://static.wikia.nocookie.net/chainsaw-man/images/1/1b/Pochita.PNG','Pochita')

```



