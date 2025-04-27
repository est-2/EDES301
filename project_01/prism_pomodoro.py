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
                       servo=board.P1_36, cs=board.P1_6, spi=board.SPI(),
                       lcd_rs=board.P2_33, lcd_en=board.P2_35, lcd_d7=board.P2_31, lcd_d6=board.P2_29, lcd_d5=board.P2_27, lcd_d4=board.P2_25,
                       ):
        """ Initialize variables and set up display """

        self.black_button       = BUTTON.Button(black_button)
        self.blue_button        = BUTTON.Button(blue_button)
        self.yellow_button      = BUTTON.Button(yellow_button)
        self.servo              = SERVO.Servo(servo)
        self.LED_matrix         = MATRIX.LEDMatrix(digitalio.DigitalInOut(cs), spi)
        self.LCD_screen         = LCD_16x2.LCD(lcd_rs, lcd_en, lcd_d7, lcd_d6, lcd_d5, lcd_d4)
        
        
        self.study_time = 0
        self.break_time = 0
        self.study_time_set = False
        self.break_time_set = False
        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""
#        self.LCD_screen.clear_screen()
        # Buttons / Servo / 
        #   - All initialized by libraries when instanitated

    # End def

    def increment_up(self, value):
        value += 5
        print(format(value))
        return value
        
    def increment_down(self, value):
        value -= 5
        print(format(value))
        return value
        

    def set_times(self):
        """Set the study time and break time using buttons"""
        
        # set study time
        self.LCD_screen.write_in_position(1, 0, "Set study time")
        print("press buttons")
        while (self.study_time_set == False):
            if self.yellow_button.is_pressed():
                self.study_time = self.study_time + 5
                time.sleep(0.5)
                print(self.study_time)
                self.LCD_screen.write("{}  ".format(self.study_time))
            if self.blue_button.is_pressed():
                self.study_time = self.study_time - 5
                time.sleep(0.5)
                print(self.study_time)
                self.LCD_screen.write("{}  ".format(self.study_time))
            if self.black_button.is_pressed():
                if (self.study_time > 0):
                    self.study_time_set = True
                else:
                    self.LCD_screen.write("INVALID TIME")
                    time.sleep(1.5)
                    self.LCD_screen.write("                ")
        self.LCD_screen.clear_screen()
        self.LCD_screen.write_two_lines("Study time:","{} minutes".format(self.study_time))
        time.sleep(3)
        
        
        # set break time
        self.LCD_screen.clear_screen()
        self.LCD_screen.write_in_position(1, 0, "Set break time")
        print("press buttons")
        while (self.break_time_set == False):
            if self.yellow_button.is_pressed():
                self.break_time = self.break_time + 1
                time.sleep(0.5)
                print(self.break_time)
                self.LCD_screen.write("{}  ".format(self.break_time))
            if self.blue_button.is_pressed():
                self.break_time = self.break_time - 1
                time.sleep(0.5)
                print(self.break_time)
                self.LCD_screen.write("{}  ".format(self.break_time))
            if self.black_button.is_pressed():
                if (self.break_time > 0):
                    self.break_time_set = True
                else:
                    self.LCD_screen.write("INVALID TIME")
                    time.sleep(1.5)
                    self.LCD_screen.write("                ")
        self.LCD_screen.clear_screen()
        self.LCD_screen.write_two_lines("Break time:","{} minutes".format(self.break_time))
    
    # End def
    
    
    def study_mode(self):
        """ display study message on LCD screen, pulse LED matrix, spin Servo """
        # write message
        self.LCD_screen.clear_screen()
        self.LCD_screen.write_two_lines("study hard!", "You got this!")
        
         # pulse the screen brightness
        self.LED_matrix.set_brightness(1)
        self.LED_matrix.light_up()
        while True:
            for i in range(12):
                self.LED_matrix.set_brightness(i)
                time.sleep(0.1)
            for i in range(12):
                self.LED_matrix.set_brightness(12-i)
                time.sleep(0.1)
                
        # spin servo
        
        
    # End def
    
    
    
    def break_mode(self):
        pass
        
    #End def
    
    
    def run(self):
        self.set_times()
        self.study_mode()
        
        
    # End def
        
        
    def cleanup(self):
        self.LCD_screen.cleanup()
        self.LED_matrix.cleanup()
        
    
    # End def
            

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the lock
    prism_pomodoro = PrismPomodoro()

    try:
        prism_pomodoro.set_times()

#    except KeyboardInterrupt:
        # Clean up hardware when exiting
#        prism_pomodoro.cleanup()
    except:
        pass


    print("study mode test")
    try:
        prism_pomodoro.study_mode()
        time.sleep(3)
        prism_pomodoro.cleanup()
    except KeyboardInterrupt:
        prism_pomodoro.cleanup()

    print("Program Complete")

