# TarkovTime
A simple python program for displaying the ingame Escape from Tarkov time in a transparent standalone window.

Download and run the prepackaged exe [TarkovTime_v1.zip](https://github.com/Bullhoff/TarkovTime/files/9693304/TarkovTime_v1.zip) or package it yourself with: 
``` pyinstaller --windowed --onefile --icon=icon.ico TarkovTime.py ```

TarkovTime originally had hotkeys, mainly for temporarly adding a background to the time to make it easier to drag, but i ended up removing it since i never used it and it gave some virus/keylogger warnings. Everything is still there to enable it again if its of interest, simply uncomment this line: 
``` #import hotkeys ```
Or download the prepackaged exe: [TarkovTime_v1_withhotkeys.zip](https://github.com/Bullhoff/TarkovTime/files/9693308/TarkovTime_v1_withhotkeys.zip)


Instructions: 
- First time you run the program a config file is generated at the file location. Most settings can only be changed in this file. 
- Doubleclick on the time to open the config menu. Press the Close or Hide button to hide it. 
- Drag on the time to move it. 
- If the ingame time isnt synced with what TarkovTime is showing, simply enter the left time displayed ingame in the textbox and press "Save" (the left ingame time have to be exactly what is in the textbox when pressing the Save button). 

![TarkovTime - Sync time](https://github.com/Bullhoff/TarkovTime/blob/main/TarkovTime-Sync.png)


TarkovTime can mess with Discords window sharing feature if you display the time over the game and at the same time share Tarkov in Discord. Placing TarkovTime on another monitor solves it. 

Works fine with OBS to display the ingame time in the recorded video:  
https://youtu.be/Kjwd7qIyjvY
