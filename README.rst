micropython-linenotify
======================

| It is a MicroPython library for sending notifications to Line
  Notify,which can be used with ESP8266 and ESP32.
| Can send both text messages, stickers and images.

github: https://github.com/PerfecXX/micropython-linenotify

Installation
============

.. code:: python

   upip install micropython-linenotify

Usage
=====

-  Create Instance and set token

.. code:: python

   line = LineNotify('<token>')

-  Notify text message

.. code:: python

   line.notify('<message>')

-  Notify sticker with text message

Sticker List:
https://developers.line.biz/en/docs/messaging-api/sticker-list/

.. code:: python

   line.notifySticker('<Sticker Package ID>','<Sticker ID>','<Message>')

-  Notify image from URL with text message

.. code:: python

   line.notifyImageURL('<Image URL>','<Message>')

Example Code
============

.. code:: python

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
