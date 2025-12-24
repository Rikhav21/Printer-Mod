# Laser cutting printer
I basically designed and build a laser cutting attatchement for a toolhead of a 3d printer. You could probably get this to work on any printer that runs klipper, but I modded my custom printer. Basically you are just going to attatch the laser to the toolhead using a bracket, and then connect it to its own PSU, and also connect it to your printer control board.
<img width="531" height="725" alt="image" src="https://github.com/user-attachments/assets/de684c25-9c58-4ab9-9c84-0fc7bb83dc0b" />
<img width="338" height="410" alt="image" src="https://github.com/user-attachments/assets/30624809-99f3-488a-b2e1-79393bcce864" />
After that you can test it by uploading my new printer config. Really all you need to know is what GPIO you are using to connect it to your printer, (I used 20) and then just adust my macros to turn it on or off. I would recommend starting at a really low value, and make sure 
that you always have your glasses on.
After that you are going to have to download change.py and input your gcode file. I used LaserGRBL and it exported as a .nc. As long as you name it input.nc you should get a folder named output.gcode that youcan upload to klipper. After that you should ust be able to run output.gcode and it will engrave your image!
<img width="491" height="397" alt="image" src="https://github.com/user-attachments/assets/174b7899-f867-4e47-985b-f84924046b80" />
<img width="481" height="443" alt="image" src="https://github.com/user-attachments/assets/e18f8cdd-2159-4334-84ef-9c757bac3f11" />
