import time
from servo import Servo  # or however you import your Servo class

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

finally:
    servo.stop_spin()