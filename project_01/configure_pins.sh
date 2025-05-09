#!/bin/bash
# --------------------------------------------------------------------------
# Prism Pomodoro - Configure Pins
# --------------------------------------------------------------------------
# License:   
# Copyright 2025 Eleanor Tucker
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this 
# list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, 
# this list of conditions and the following disclaimer in the documentation 
# and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its contributors 
# may be used to endorse or promote products derived from this software without 
# specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# --------------------------------------------------------------------------
# 
# Configure pins for Pomodoro Prism:
#   - LCD (GPIO)
#   - Buttons (GPIO)
#   - Servo (PWM)
#   - LED matrix (GPIO, SPI)
# 
# --------------------------------------------------------------------------

# LCD
config-pin P2_25 gpio
config-pin P2_27 gpio
config-pin P2_29 gpio
config-pin P2_31 gpio
config-pin P2_33 gpio
config-pin P2_35 gpio

# Buttons
config-pin P2_02 gpio
config-pin P2_04 gpio
config-pin P2_06 gpio

# Servo
config-pin P1_36 pwm

# LED matrix
config-pin P1_06 gpio
# config-pin P1_08 spi gives error
config-pin P1_10 spi
config-pin P1_12 spi
