# SendPhotoAndVideo_withRPI_OnTelegram
Come fare foto e video con Raspberry Pi Cam e Telegram

I materiali da utilizzare sono i seguenti:

* Raspberry Pi
* Pi camera
* Tastiera
* Mouse
* Monitor
* Telegram
* Connessione a internet

# INSTALLAZIONI PRELIMINARI

ATTENZIONE: questa procedura è valida solo per la Raspberry Pi Camera, non funzionerà con una webcam USB

Apri il terminale.

Per sicurezza effettuiamo un update:

`sudo apt-get update
sudo apt-get upgrade`

Per l’implementazione del bot occorre una specifica libreria. Per installare questa libreria basta eseguire il comando.

`pip install telepot`

# INSTALLAZIONE RASPBERRY PI CAMERA

Ho scritto una guida approfondito a riguardo, per leggerla potete utilizzare il seguente link: [Come installare e configurare la Raspberry Pi Camera](http://moreware.org/wp/blog/2021/08/29/come-configurare-e-installare-la-raspberry-pi-camera/)

INSTALLAZIONE RASPBERRY PI CAMERA

Ho scritto una guida approfondito a riguardo, per leggerla potete utilizzare il seguente link: Come installare e configurare la Raspberry Pi Camera

# Creazione bot

Il primo passo consiste nell’aprire l’applicazione telegram. Una volta aperta cerchiamo “BotFather” tramite la funzione cerca cliccando sull’apposita lente di ingrandimento.

“BotFather” è un bot che permette di creare altri bot.

Avviamo il bot scrivendo “/start“, poi premiamo invio.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/bothfather1.png?w=623&ssl=1)

Per creare un nuovo bot digitiamo “/newbot”.

BotFather ci chiederà di assegnare un nome al nostro nuovo Bot, basta digitare un qualsiasi nome e poi premere Invio.

Dobbiamo anche inserire un username che lo renderà riconoscibile pubblicamente. Username deve terminare in “Bot” o ” _bot”.

In seguito alla assegnazione del nome e dell’username BotFather ci comunicherà informazioni importanti in seguito per compilare il codice per il funzionamento della camera e dell’invio dati. ATTENZIONE: QUESTE INFOMAZIONI LE DOVREMMO TENERE SOLO PER NOI. La prima parte riguarda il percorso per trovare il nostro bot. La seconda è la API che sarà utilizzato nel nostro codice.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/botfather2.png?w=618&ssl=1) 

# [CODICE](https://github.com/SimoneMoreWare/SendPhotoAndVideo_withRPI_OnTelegram) 

(N.B: nel codice ho utilizzato telepot, ma oramai questa libreria è abbandonata, il progetto l ho fatto tanto tempo fa, consiglio di usare librerie più aggiornate come telebot o PyTelegramAPI

