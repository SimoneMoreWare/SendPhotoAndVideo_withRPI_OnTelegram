#!/usr/bin/python
import time
import telepot
import picamera

def handle(msg):

   chat_id = msg['chat']['id']
   command = msg['text']

   print ('Got command: %s' % command)

   if command == '/uptime':
       var1 = commands.getoutput("uptime")
       bot.sendMessage(chat_id,var1)

   elif command == '/start':
       bot.sendMessage(chat_id,"Ciao, bentornato. Digita /connesso per sapere se è tutto ok. Digita /foto o /video per ricevere foto o video")
  
   elif command == '/connesso':
       bot.sendMessage(chat_id,"Camera connessa")
   
   #scatto foto
   elif command == '/foto':
       bot.sendMessage(chat_id,"Ciao eccoti la foto")
       camera=picamera.PiCamera()
       camera.capture('./capture.jpg')
       camera.close()

       # Invia foto alla chat
       bot.sendPhoto(chat_id=chat_id, photo=open('./capture.jpg', 'rb'))

   elif command == '/video':
       bot.sendMessage(chat_id,"A breve arrivera il video")
       camera= picamera.PiCamera()
       camera.start_recording('video.h264')
       time.sleep(5)
       camera.stop_recording()

       # invia video alla chat
       bot.sendVideo(chat_id=chat_id, video=open('video.h264', 'rb'))

#sostituisci la tua api key
bot = telepot.Bot('yourapikey')
bot.message_loop(handle)
print ('Sono pronto…')

while 1:
    time.sleep(10)

