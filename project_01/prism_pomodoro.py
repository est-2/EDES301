"""
--------------------------------------------------------------------------
Prism Pomodoro
--------------------------------------------------------------------------
License:   
Copyright 2025 Eleanor Tucker

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use the following hardware components to make a prism pomodoro:  
  - 16x2 LCD display
  - 3 Buttons
  - MAX7219 LED matrix driver and 8x8 LED matrix
  - Servo

Requirements:
  - Hardware:
    - 
    
Uses:
  - 

"""
import time
import board

import digitalio

import adafruit_character_lcd.character_lcd as characterlcd

import LED_matrix    as MATRIX
import button        as BUTTON
import servo         as SERVO
import LCD_16x2      as LCD_16x2


# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class PrismPomodoro():
    """ PrismPomodoro """
    
    black_button    = None
    blue_button     = None
    yellow_button   = None
    servo           = None
    LED_matrix      = None
    LCD_screen      = None
    cs              = None
    spi             = None
    lcd_rs          = None
    lcd_en          = None
    lcd_d7          = None
    lcd_d6          = None
    lcd_d5          = None
    lcd_d4          = None
    
    def __init__(self, black_button="P2_2", blue_button="P2_4", yellow_button="P2_6",
                       servo="P1_36", cs=board.P1_6, spi=board.SPI(),
                       lcd_rs=board.P2_33, lcd_en=board.P2_35, lcd_d7=board.P2_31, lcd_d6=board.P2_29, lcd_d5=board.P2_27, lcd_d4=board.P2_25,
                       study_time=0, break_time=0):
        """ Initialize variables and set up display """

        self.black_button       = BUTTON.Button(black_button)
        self.blue_button        = BUTTON.Button(blue_button)
        self.yellow_button      = BUTTON.Button(yellow_button)
#        self.servo              = SERVO.Servo(servo, default_position=SERVO_LOCK)
        self.LED_matrix         = MATRIX.LEDMatrix(digitalio.DigitalInOut(cs), spi)
        self.LCD_screen         = LCD_16x2.LCD(lcd_rs, lcd_en, lcd_d7, lcd_d6, lcd_d5, lcd_d4)
        
        self.study_time = study_time
        self.break_time = break_time
        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""
        self.LCD_screen.clear_screen()
        # Buttons / Servo / 
        #   - All initialized by libraries when instanitated

    # End def

    def set_study_time(self):
        """Set the study time"""
        self.LCD_screen.write_in_position(0, 12, ",  '")
        self.LCD_screen.write_in_position(1, 0, "Set study time")
        while(self.black_button.is_pressed() == False):
            print("ready for buttons")
            if (self.yellow_button.is_pressed() == True):
                self.study_time = self.study_time + 5
                print("yellow pressed")
                self.LCD_screen.write(format(self.study_time))
            if (self.blue_button.is_pressed() == True):
                self.study_time = self.study_time - 5
                print("blue pressed")

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the lock
    prism_pomodoro = PrismPomodoro()

    try:
        # Run the lock
       # combo_lock.run()
       prism_pomodoro.set_study_time()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
       # combo_lock.cleanup()
       pass

    print("Program Complete")

