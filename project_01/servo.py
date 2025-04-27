"""
--------------------------------------------------------------------------
Continuous Rotation Servo Driver
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

SG90 Servo Driver

API:
  Servo(pin)
    - Provide pin that the Servo is connected
  
    turn(percentage)
      -   0 = Fully clockwise
      - 100 = Fully anti-clockwise

"""
import time
import board
import pwmio
from adafruit_motor import servo

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

class Servo():
    
    pin     = None
    status  = None
    
    def __init__(self, pin=board.P1_36):
        """ Initialize variables and set up the Servo """
        if (pin == None):
            raise ValueError("Pin not provided for Servo()")
        else:
            self.pin = pwmio.PWMOut(pin, frequency=50)
        
        self.servo = None
        self.status = None
        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""        
        # Initialize Servo
        self.servo = servo.ContinuousServo(self.pin)
        
    # End def

    
    def spin_forward(self):
        self.servo.throttle = 0.2
        self.status = "forward"

    # End def
    
    
    def spin_backward(self):
        self.servo.throttle = -0.2
        self.status = "backward"
        
    # End def


    def stop_spin(self):
        self.servo.throttle = 0.0
        self.status = "stopped"
    
    # End def
    

    def cleanup(self):
        """Cleanup the hardware components."""
        # Stop servo
        self.stop_spin()
        self.pin.deinit()
        
    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
 
    print("Servo Test")

    # Create instantiation of the servo
    servo = Servo("P1_36")

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    print("Use Ctrl-C to Exit")
    
    try:
        servo.spin_forward()
        print(servo.status)
        time.sleep(3)
        servo.stop_spin()
        print(servo.status)
        time.sleep(3)
        servo.spin_backward()
        print(servo.status)
        time.sleep(3)
        print(servo.status)
        
    except KeyboardInterrupt:
        pass

    # Clean up hardware when exiting
    servo.cleanup()

    print("Test Complete")

