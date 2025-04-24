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

import LED_matrix    as MATRIX
import button        as BUTTON
import servo         as SERVO
import LCD_16x2      as LCD


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
    
    
    
    reset_time     = None
    button         = None
    red_led        = None
    green_led      = None
    potentiometer  = None
    servo          = None
    display        = None
    music          = None
    debug          = None
    
    def __init__(self, reset_time=2.0, button="P2_2", 
                       red_led="P2_6", green_led="P2_4",
                       potentiometer="P1_19", servo="P1_36", 
                       i2c_bus=1, i2c_address=0x70, buzzer="P2_1", debug=False):
        """ Initialize variables and set up display """

        self.reset_time     = reset_time
        self.button         = BUTTON.Button(button)
        self.red_led        = LED.LED(red_led)
        self.green_led      = LED.LED(green_led)
        self.potentiometer  = POT.Potentiometer(potentiometer)
        self.servo          = SERVO.Servo(servo, default_position=SERVO_LOCK)
        self.display        = HT16K33.HT16K33(i2c_bus, i2c_address)
        self.music          = MUSIC.BuzzerMusic(buzzer)
        self.debug          = debug
        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""

        # Initialize Display
        self.set_display_dash()

        # Button / LEDs / Potentiometer / Servo 
        #   - All initialized by libraries when instanitated

    # End def


    def lock(self):
        """Lock the lock:
               - Turn on red LED; Turn off green LED
               - Set servo to closed
        """
        if self.debug:
            print("lock()")
        
        # Set LEDs
        self.red_led.on()
        self.green_led.off()
        
        # Set servo to "locked"
        self.servo.turn(SERVO_LOCK)

    # End def


    def unlock(self):
        """Unlock the lock.
               - Turn off red LED; Turn on green LED
               - Set servo to open
               - Set display to "----"
        """
        if self.debug:
            print("unlock()")
            
        # Set LEDs
        self.red_led.off()
        self.green_led.on()

        # Set servo to "unlocked"
        self.servo.turn(SERVO_UNLOCK)

        # Set display to dash
        self.set_display_dash
        
        # Play song
        self.music.play_song_from_list(1)

    # End def


    def show_analog_value(self):
        """Show the analog value on the screen:
               - Read raw analog value
               - Divide by 4 (remove two LSBs)
               - Display value
               - Return value
        """
        if self.debug:
            print("show_analog_value()")
            
        # Read value from Potentiometer
        value = self.potentiometer.get_value()

        # Divide value by POT_DIVIDER
        value = value // POT_DIVIDER

        # Update display (must be an integer)
        self.display.update(value)
        
        # Return value
        return value

    # End def


    def input_combination(self):
        """Input a combination for the lock:
               - Wait for a button press doing nothing (start of user inputing combination)
               - Repeat 3 time:
                 - Wait for button press; show analog value
                 - Record analog value
               - Return combination
        """
        # Initialize combination array
        combination = [None, None, None]
        
        for i in range(3):
            # i gets value 0, 1, 2
            
            # Update display with current input
            self.set_display_input(i+1)

            # Wait for button press (do nothing)
            self.button.wait_for_press()
            
            # Set button unpressed callback function
            self.button.set_unpressed_callback(self.show_analog_value)
            
            # Wait for button press (show analog value)
            self.button.wait_for_press()
            
            # Get callback function value from button
            value = self.button.get_unpressed_callback_value()
            
            # Remove button unpressed callback function
            self.button.set_unpressed_callback(None)

            # Record Analog value
            combination[i] = value

        if self.debug:
            print(combination)
            
        return combination

    # End def


    def run(self):
        """Execute the main program."""
        combination                  = [None, None, None]  # Combination
        combo_attempt                = [None, None, None]  # Combination attempt
        program                      = True
        
        # Unlock the lock
        self.unlock()        
        time.sleep(1)
                
        while(1):
            
            # Program the lock
            if (program):
                if self.debug:
                    print("Program Lock")
                
                # Set display
                self.set_display_prog()
                
                # Wait for button press (do nothing)
                self.button.wait_for_press()
                
                # Get combination
                combination = self.input_combination()
                
                # Lock the lock
                self.lock()
        
                # Set program lock to False
                program = False

            # Set Display to try combination
            self.set_display_try()

            # Wait for button press (do nothing)
            self.button.wait_for_press()
            
            # Get combination
            combo_attempt = self.input_combination()

            # Compare attempt against combination
            combo_pass = True

            for i in range(2):
                if combination[i] != combo_attempt[i]:
                    combo_pass = False

            # If combination passed
            if combo_pass:
                if self.debug:
                    
                    print("Combination Passed")
                # Unlock the lock
                self.unlock()

                # Wait for button press
                self.button.wait_for_press()
                
                # Get press duration
                duration = self.button.get_last_press_duration()
                
                # If greater than reset_time, program lock, else lock the lock
                if (duration > self.reset_time):
                    program = True
                else:
                    self.lock()
            
            time.sleep(1)

    # End def


    def set_display_prog(self):
        """Set display to word "Prog" """
        self.display.text("Prog")

    # End def


    def set_display_try(self):
        """Set display to word " go " """
        self.display.text(" go ")

    # End def


    def set_display_input(self, number):
        """Set display to word "in: #" """
        self.display.text("in {0}".format(number))

    # End def


    def set_display_dash(self):
        """Set display to word "----" """
        self.display.text("----")

    # End def


    def cleanup(self):
        """Cleanup the hardware components."""
        
        # Set Display to show program is complete
        self.display.text("done")

        # Clean up hardware
        self.button.cleanup()
        self.red_led.cleanup()
        self.green_led.cleanup()
        self.potentiometer.cleanup()
        self.servo.cleanup()
        self.music.cleanup()

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

