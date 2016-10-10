# sprueche-bot

NOTE: As this bot is based on a german Facebook page, all further documentation
      will be written in german.

### Wofür ist dieser Bot?
 - Er holt sich die neuesten Posts der Seite WillyNachdenklich von Facebook
 - Und schickt sie weiter in einen Telegram Chat

### Wie richte ich das ganze auf meinem System ein?
 - Erstmal braucht man ein Facebook-Entwickler Konto
 - Dann muss man dort eine neue App erstellen, um Zugriff auf die Graph-API zu
   bekommen
 - Die App-ID und das App-Secret muss man in der Datei `fb_app.json` eintragen
 - Dann erstellt man einen Telegram Bot, und speichert das Token in der Datei
   `tg_bot.json`
 - Der Bot ist ziemlich primitiv und schreibt nur ein einen Chat, deshalb muss
   die Chat-ID auch in der Konfigurationsdatei gespeichert werden
   (An die Chat-ID kommt man über die `getUpdates` Funktion der Telegram API)
 - Jetzt einfach `bot.py` ausführen (am besten in einem regelmäßigen Intervall)

### Was ist der Sinn dieses Bots?
 - Kein konkreter, einfach ein bisschen Spaß verbreiten :joy:
 - Und jetzt viel Vergnügen!
