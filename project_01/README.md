# Pomodoro Prism Project
Rice University EDES301 Spring 2025
Eleanor Tucker


## Description
This code operates a Prism Pomodoro -- a study timer that uses visual instead of auditory cues. It runs using python scripts on a PocketBeagle. For details on the hardware and story of this project, visit [this hackster.io page](hackster.io)


## Software requirements
Libraries: (*Note: some of these libraries require Python 3.11*)
- Time
- Board
- Digitalio
- Adafruit_BBIO
- Adafruit\_character_lcd
- Adafruit_max7219
- Adafruit_motor

## Code structure
The code uses object-oriented programming and creates instantiations from classes. Each object corresponds to a hardware component (or the device as a whole).
Classes and objects in prism_pomodoro.py: 
- MATRIX class --> one object (LED_matrix)
- BUTTON class --> three objects (black\_button, blue\_button, and yellow_button)
- SERVO class --> one object (servo)
- LCD\_16x2 class --> one object (LCD_screen)
- PrismPomodoro class --> one object (prism_pomodoro)


## How to run
To run this code, you will need to download the 5 python files, configure pins script, and run script. Be sure to edit the run script to reflect the location of the files, and the configure pins script to reflect the correct pins for your set-up.


## Using the Prism Pomodoro
First, you will be prompted to set the study and break times. Use the yellow button to increase the value, and the blue button to decrease the value. Once the screen displays your desired value (in mintues), press the black button to confirm. Then, the device will automatically enter study mode and switch to break mode according to the times you entered. 

