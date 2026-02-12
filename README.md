# Laser cutting printer
## Overview
I basically designed and build a laser cutting attatchement for a toolhead of a 3d printer. You could probably get this to work on any printer that runs klipper, but I modded my custom printer
<img width="531" height="725" alt="image" src="https://github.com/user-attachments/assets/de684c25-9c58-4ab9-9c84-0fc7bb83dc0b" />
<img width="338" height="410" alt="image" src="https://github.com/user-attachments/assets/30624809-99f3-488a-b2e1-79393bcce864" />
## The build
For the build all that you would need to do is attatch the laser to the toolhead using a bracket, which I just printed in PLA. You are most likely going to have  You can look at the CAD [here](https://cad.onshape.com/documents/d856a3708ade0f004ee6e4d1/w/7b963df3d5215184ce110ce8/e/33774b02b25fc0851c569ffd?renderMode=0&uiState=6982892e924df17039e1cd59)
<img width="612" height="736" alt="image" src="https://github.com/user-attachments/assets/447de6f0-d8a4-4486-b5ef-65573a013193" />
## The electronics
For the electronics, all you have to do is connect the laser PSU to it's controller. Then I connected the ground and controller pin of my mainboard to the DC in and ground on our laser controller. Finally I just plugged in the lasser pins to the controlboard and that should be all of the wiring.
<img width="1042" height="790" alt="530048269-61fd2402-6133-4082-97aa-afdab45ca0bf" src="https://github.com/user-attachments/assets/01625bab-affd-4d24-b531-88f714ba3b1d" />
## The firmware
After that you can test it by uploading my new printer config. Really all you need to know is what GPIO you are using to connect it to your printer, (I used 20) and then just adust my macros to turn it on or off. I would recommend starting at a really low value, and make sure that you always have your glasses on.
After that you are going to have to download change.py and input your gcode file. I used LaserGRBL and it exported as a .nc. As long as you name it input.nc you should get a folder named output.gcode that youcan upload to klipper. After that you should ust be able to run output.gcode and it will engrave your image!

<img width="489" height="340" alt="530050401-e7ebefd4-ec5e-4e9c-b518-6d1618c2aaa8" src="https://github.com/user-attachments/assets/bfaa88c0-2faa-429e-8085-0104b7db7321" />
<img width="491" height="397" alt="image" src="https://github.com/user-attachments/assets/174b7899-f867-4e47-985b-f84924046b80" />
<img width="481" height="443" alt="image" src="https://github.com/user-attachments/assets/e18f8cdd-2159-4334-84ef-9c757bac3f11" />
## BOM
| Item | Description                                           | Supplier Link                                                      | Unit Price (USD) | Qty |      Total |
| ---: | ----------------------------------------------------- | ------------------------------------------------------------------ | ---------------: | --: | ---------: |
|    1 | Laser Module (≈80W optical class, AliExpress listing) | [AliExpress](https://www.aliexpress.us/item/3256804434878907.html) |           $40.00 |   1 |     $40.00 |
|    2 | Power Supply Unit (PSU)                               | [AliExpress](https://www.aliexpress.us/item/3256807006443600.html) |           $12.00 |   1 |     $12.00 |
|      | **Total Cost**                                        |                                                                    |                  |     | **$52.00** |
