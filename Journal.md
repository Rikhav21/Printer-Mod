# Laser cutter 
#### By @Rikhav
Time spent 28 nand a half hours
## Day 1
So today I mainly ust worked on research took an inventory on parts that I had, and sort of thought about how to build this thing. I found something really cool where someone
[attatches a laser cutter to their A1 mini](https://www.reddit.com/r/BambuLab/comments/1oi44fl/i_turned_my_bambu_a1_mini_into_a_mini_laser_cutter/) 
so I was thinking that I can domehitn gsimilar to that. Today I was mainly looking at wiring, how I would actually do it, adustability etc.

<img width="352" height="532" alt="image" src="https://github.com/user-attachments/assets/de8ab592-ae5d-4f43-8697-117f6358399a" />

Total time spent : 3 and a half hours.
## Day 2
So today I went more down the laser cutting rabit hole and actually saw different designs that people implemented. I decided that it would probably be better if I modded mmy custom printer (inspired by the 100) instead of my bambu labs, because I ust know how it works a lot better. However, I also did realize that my laser does operate at a different voltage than the rest of my printer so I am going to have to use a seperate PSU for that. I also loked more into the mounting solutions, and I decided on a 3d printed bracket that can hold a sliding frame.
<img width="703" height="736" alt="image" src="https://github.com/user-attachments/assets/a2724606-300f-43ea-8476-5c2e2c17c009" />

Total time spend : 4 hours.
## Day 3
Today I meainly spent time on actually getting the elctronics done, so I soldered the wires, tested connections before powering it on, because it's pretty high voltage, stuff, and triple checking that everything was wired correctly before giving it power. Here I didn't have a barrel ack for DC input to the laser controller, so instead I ust soldered on the wires to the back of the board with the exposed socket terminals. I did test it where I turned it on,a nd the laser was at 0.1% power, and I was able to see a faint blue glow so it does work. tomorrow I am going to try to mount and actuallycut something.
time spent: 4 hours

## Day 4
Today I ust wanted to finish the assembly portion and try powering everything on. it turned out that actually connecting the laser controll board to the SKR pico was a little bit harder than I thought, because the board was out of reach, and the wires to the laser restricted its movement so I had to make them longer. I had to redeigsn the mount because the first one did  not fit that well,a nd I had to print at about 50% infill because it was supporting almost the entire weight of the laser. Although the toolhead is now heavier, it doe snot seem to actually change the movement of the laser that much.
time spend: 3 and a half hours.

## Day 5
Today I tried to do firmware. I actually had a lot of trouble figuring out how to controll the laser through klipper, and so I ended up just addressing the GPIO pin directly through macros to turn the GPIO on or off. this actually toook a lot longer than I expected, but the laser is turning on at 5% of full power, and is able to start burning wood.I also researched a bit more about actually slicng laser G-code and I decided on uring LaserGRBL for that, but I will actually start slicing code tomorrow.
Time spent: 2 hours

## Day 6
Today was another firmware day. I tried to make it so that I can controll the amount that the laser turns on based on the value that I send it,a nd I got that macro working. Then I learned how to use LaserGRBL, and sliced my first image of a square. after exporting it, I realized that it was exported with a .nc file extensions, so I could import it into klipper, but I was not able to get it to run, I tried a few different things, but at the end it turns out that just changing the file extension to .gcode actually works perfectly. Although I was able to get the code to atleast start compiling, it was still giving errors about unrecognized commands so I will look into that tomorrow.
Time spent : 3 hours

## Day 7
Today I tried to look into what was actually causing the errors, and realized that the g-code that LaserGRBL exported was actually not able to run on klipper because it did not recognize S80 or something like that sa a command, so I tried to set up macros so that klipper could tell that I was trying to turn on the laser. That didn't work either because S90 had to be written as S S-90; And I had no idea how to do that. I trid finding and replacing all of those, however I got some complaints that I think I can fix by moving the macros to a new line, but I am going to work on that tommorrow.
Time spent:  4 hours

## Day 8
Today I continued to work on the firmware for the mod, and once again it turned out harder than I expected, because after seperating all the lines, you need to add semi colos back to the end of the line that you seperated, so instead I spend an hour writing a python script to do that for me, and how I am finally able to execute the code that I sliced with lightburn, as my script ust inputs the .nc file that you get out of LaserGRBL, and converts it to a .gcode file that klipper coudl read. I hadm't donw any calibration yet, but the laser was able to mark the surface of the scrap wook.
Time spent 4 and a half hours.
