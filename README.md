# Pygame with sockets

This repo was created spontaneously for researchers like me to get started with such pointless ideas as **sockets with pygame**!
The engine was code is based on [DaFluffyPotato's](https://www.youtube.com/@DaFluffyPotato) videos, please go subscribe to him.

Right now, on version 1 the server works only in local network and can be used on 1 laptop only. Which easily fixed if you can input another player's ip. Go check it code.

## The essence of the project
1. You start a server somewhere. Please pay attention, you can connect to accurate ip in your local network or to a global ip. You have to specify that.
2. You start the game.py, you're client now. You try to connect to server (you have to know server's ip and port), server listens to you and catches.
3. The data from client is sent to server, then processed and translated to needed clients.
   - The data here is realized this way:
      Header (1000 bytes), contains the size of message and some extra data if needed;
      Json-typed info, the message.
   - There is probably a way to send whole pygame object.
   - Many messages can be read at one time with use of "threading" library. Might be exchanged by multiprocassing or other ways.
