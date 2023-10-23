import time
import pigpio

# GPIO number. On a rapsberry pi 1, the hardware PWM pin is
# GPIO(HPWM0) 12 and (HPWM1)13
ROL_PIN = 12
PIT_PIN = 13
THR_PIN = 20
YAW_PIN = 21

# Delay in seconds to wait after sending a signal
DELAY     = 0.01

# Minimum duty cycle, in milliseconds
MIN_DUTYCYCLE = 1002

# Maximum duty cycle, in milliseconds
MAX_DUTYCYCLE = 2007

# Fail Safe values, in milliseconds
FS_DUTYCYCLE = 1502

pi = pigpio.pi()
pi.set_mode(PIT_PIN, pigpio.OUTPUT)
pi.set_mode(ROL_PIN, pigpio.OUTPUT)
pi.set_mode(YAW_PIN, pigpio.OUTPUT)
pi.set_mode(THR_PIN, pigpio.OUTPUT)

time.sleep(1)

# Set to Fail Safe values
pi.set_servo_pulsewidth(PIT_PIN, FS_DUTYCYCLE)
pi.set_servo_pulsewidth(ROL_PIN, FS_DUTYCYCLE)
pi.set_servo_pulsewidth(YAW_PIN, FS_DUTYCYCLE)
pi.set_servo_pulsewidth(THR_PIN, 1100)
time.sleep(5)

try:
    while True:
        for pulse in range(MIN_DUTYCYCLE, MAX_DUTYCYCLE):
            pi.set_servo_pulsewidth(PIT_PIN, pulse)
            pi.set_servo_pulsewidth(ROL_PIN, pulse)
            pi.set_servo_pulsewidth(YAW_PIN, pulse)
            pi.set_servo_pulsewidth(THR_PIN, pulse)
            time.sleep(DELAY)

        for pulse in range(MAX_DUTYCYCLE, MIN_DUTYCYCLE, -1):
            pi.set_servo_pulsewidth(PIT_PIN, pulse)
            pi.set_servo_pulsewidth(ROL_PIN, pulse)
            pi.set_servo_pulsewidth(YAW_PIN, pulse)
            pi.set_servo_pulsewidth(THR_PIN, pulse)
            time.sleep(DELAY)
except Exception as e:
    print (e)
    pi.stop()
