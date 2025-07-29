from gpiozero import Servo
from time import sleep

s1 = Servo(11,min_pulse_width=500/1000000,max_pulse_width=2500/1000000)
s2 = Servo(13,min_pulse_width=500/1000000,max_pulse_width=2500/1000000)

while True:
    print("moving to -1")
    s1.value = -1
    s2.value = -1
    sleep(2)

    print("moving to 0")
    s1.value = 0
    s2.value = 0
    sleep(2)

    print("moving to 1")
    s1.value = 1
    s2.value = 1
    sleep(2)
