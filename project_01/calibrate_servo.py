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

FS5103R Continous Rotation Servo Calibration code
    

"""
import time
from servo import Servo
 
 
servo = Servo()  # or Servo("P1_36") if not default
 
print("Calibrating... Press Ctrl+C to stop.")
 
throttle = 0.0
step = 0.01
 
try:
    while True:
        servo.servo.throttle = throttle
        print(f"Trying throttle = {throttle}")
        time.sleep(1.5)
 
        direction = input("Did it move? (y/n): ").strip().lower()
        if direction == "n":
            print(f"Neutral value found: {throttle}")
            break
 
        # Try next value (adjust up or down)
        throttle -= step
 
except KeyboardInterrupt:
    print("Calibration stopped.")