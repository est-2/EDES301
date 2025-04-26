"""
--------------------------------------------------------------------------
LCD 16x2 Driver
--------------------------------------------------------------------------
License:   
Copyright 2021-2025 - Eleanor Tucker

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



Software API:

  Button(pin, press_low)
    - Provide pin that the button monitors
    
    wait_for_press()
      - Wait for the button to be pressed 
      - Function consumes time
        
    is_pressed()
      - Return a boolean value (i.e. True/False) on if button is pressed
      - Function consumes no time
    
    get_last_press_duration()
      - Return the duration the button was last pressed

    cleanup()
      - Clean up HW
      
    Callback Functions:
      These functions will be called at the various times during a button 
      press cycle.  There is also a corresponding function to get the value
      from each of these callback functions in case they return something.
    
      - set_pressed_callback(function)
        - Excuted every "sleep_time" while the button is pressed
      - set_unpressed_callback(function)
        - Excuted every "sleep_time" while the button is unpressed
      - set_on_press_callback(function)
        - Executed once when the button is pressed
      - set_on_release_callback(function)
        - Executed once when the button is released
      
      - get_pressed_callback_value()
      - get_unpressed_callback_value()
      - get_on_press_callback_value()
      - get_on_release_callback_value()      


"""
import time
import board
import adafruit_character_lcd.character_lcd as characterlcd
import digitalio

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class LCD():
    """ LCD Class """
    lcd_rs = None
    lcd_en = None
    lcd_d7 = None
    lcd_d6 = None
    lcd_d5 = None
    lcd_d4 = None
    
    
    def __init__(self, lcd_rs=board.P2_33, lcd_en=board.P2_35, lcd_d7=board.P2_31, lcd_d6=board.P2_29, lcd_d5=board.P2_27, lcd_d4=board.P2_25):
        """ Initialize variables and set up the button """
        if (lcd_rs == None or lcd_en == None or lcd_d7 == None or lcd_d6 == None or lcd_d5 == None or lcd_d4 == None):
            raise ValueError("Pins not provided for LCD")
        else:
            self.lcd_rs = lcd_rs
            self.lcd_en = lcd_en
            self.lcd_d7 = lcd_d7
            self.lcd_d6 = lcd_d6
            self.lcd_d5 = lcd_d5
            self.lcd_d4 = lcd_d4
              
        self.lcd = characterlcd.Character_LCD_Mono(digitalio.DigitalInOut(lcd_rs), digitalio.DigitalInOut(lcd_en), digitalio.DigitalInOut(lcd_d4), digitalio.DigitalInOut(lcd_d5), digitalio.DigitalInOut(lcd_d6), digitalio.DigitalInOut(lcd_d7), 16, 2)

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        self.lcd.clear()
    # End def

    
    def cleanup(self):
        """ Clean up the hardware. """
        self.lcd.clear()
    
    # End def
    
    
    def clear_screen(self):
        """ Clear the screen """
        self.lcd.clear()
        
    # End def
    
    def write(self, first_line):
        """ write a message on the LCD """
        self.lcd.message = first_line
        
    # End def

        
    def write_in_position(self, row, col, string):
        """ write a message in a specific place on the LCD """
        # The LCD has 2 rows, and 16 columns, so the row should be 0 or 1 and col should be 0-15
        # Create the message string with an appropriate number of newlines to position the cursor.
        if row == 0:
            # Top row
            self.lcd.message = " " * col + string
        elif row == 1:
            # Bottom row
            self.lcd.message = "\n" + " " * col + string
        
    # End def
        
   
    
# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("LCD Test")

    # Create instantiation of the LCD screen
    lcd = LCD(board.P2_33, board.P2_35, board.P2_31, board.P2_29, board.P2_27, board.P2_25)
  #  print("hi {0}".format(dir(board)))
    
    lcd.clear_screen()
    lcd.write("test")
    time.sleep(3)
    lcd.clear_screen()
    time.sleep(3)
    lcd.write_in_position(0,0,"testing")
    lcd.write_in_position(1,4,"position")
    time.sleep(3)
    lcd.cleanup()

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    try:
        pass
    except KeyboardInterrupt:
        pass

    print("Test Complete")

