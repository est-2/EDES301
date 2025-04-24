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

import adafruit_character_lcd.character_lcd as characterlcd

import LED_matrix    as MATRIX
import button        as BUTTON
import servo         as SERVO


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
                       servo="P1_36", cs=board.P1_6, spi=board.SPI()):
        """ Initialize variables and set up display """

        self.black_button       = BUTTON.Button(black_button)
        self.blue_button        = BUTTON.Button(blue_button)
        self.yellow_button      = BUTTON.Button(yellow_button)
        self.servo              = SERVO.Servo(servo, default_position=SERVO_LOCK)
        self.LED_matrix         = MATRIX.LEDMatrix(cs, spi)
        
        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""

        # Buttons / Servo / 
        #   - All initialized by libraries when instanitated

    # End def



# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the lock
    combo_lock = CombinationLock(debug=False)

    try:
        # Run the lock
        combo_lock.run()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        combo_lock.cleanup()

    print("Program Complete")

