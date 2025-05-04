"""
--------------------------------------------------------------------------
LED Matrix Driver
--------------------------------------------------------------------------
License:   
Copyright 2025 - Eleanor Tucker

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

LED Matrix Driver

  This driver works with the MAX7219 LED matrix driver. 


Software API:

  LEDMatrix(cs, spi)
    - Inputs: 
        cs  - pin configured by digitalio
        spi - SPI as defined by board
    
    set_brightness(value)
      - Changes the brightness of the LED matrix
      - Value ranges from 1 (dimmest) to 15 (brightest)
      
    light_up()
      - All LEDs light up
    
    go_dark()
      - All LEDs turn off
      
    cleanup()
      - LEDs turn off


"""
import time
import board
import digitalio
from adafruit_max7219 import matrices

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class LEDMatrix():
    """ LEDMatrix Class """
    cs                  = None
    spi                 = None
    
    
    def __init__(self, cs=digitalio.DigitalInOut(board.P1_6), spi=board.SPI()):
        """ Initialize variables and set up the LED matrix """
        if (cs == None or spi == None):
            raise ValueError("Pins not provided for LEDMatrix()")
        else:
            self.cs     = cs
            self.spi    = spi

        self.matrix = matrices.Matrix8x8(self.spi, self.cs)

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize LED matrix, clear the display
        time.sleep(0.1)
        self.matrix.fill(False)
        self.matrix.show()
        
    # End def
    
    
    def set_brightness(self, value):
        """ Change brightness of LED Matrix """
        # values range from 1 to 15
        self.matrix.brightness(value)
        
    # End def
    
    
    def light_up(self):
        """ Light up LED matrix completely """
        self.matrix.fill(True)
        self.matrix.show()
        
    # End def
    
    
    def go_dark(self):
        """ Clear/turn off the matrix display """
        self.matrix.fill(False)
        self.matrix.show()
        time.sleep(0.1)
        
    # End def
    
    
    def cleanup(self):
        """ Clean up the hardware. """
        # Clear the display
        self.matrix.fill(False)
        self.matrix.show()
    
    # End def
    
    
# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Test")

    # Create instantiation of the LED matrix
    ledMatrix = LEDMatrix(digitalio.DigitalInOut(board.P1_6), board.SPI())
    
    print("light up now")
    ledMatrix.light_up()
    time.sleep(3)
    ledMatrix.cleanup()
    
    try:
        pass
    except KeyboardInterrupt:
        pass

    print("Test Complete")

