import RPi.GPIO as GPIO
import time

xpin = 11
ypin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(xpin, GPIO.OUT)
GPIO.setup(ypin, GPIO.OUT)

x = GPIO.PWM(xpin, 50) # GPIO 17 for PWM with 50Hz
y = GPIO.PWM(ypin, 50)
x.start(2.5) # Initialization
y.start(2.5)
try:
  while True:
    testsweep(x,0,150)
    testsweep(y,0,150)

except KeyboardInterrupt:
  x.stop()
  y.stop()
  GPIO.cleanup()

def testsweep(s,l,h):
  for n in range(l,h):
    d = n/10
    print('duty',d)
    s.ChangeDutyCycle(d)
    time.sleep(.5)
  for n in range(h,l):
    d = n/10
    print('duty',d)
    s.ChangeDutyCycle(d)
    time.sleep(.5)

def periodicsweep():
  x.ChangeDutyCycle(5)
  y.ChangeDutyCycle(5)
  time.sleep(0.5)
  x.ChangeDutyCycle(7.5)
  y.ChangeDutyCycle(7.5)
  time.sleep(0.5)
  x.ChangeDutyCycle(10)
  y.ChangeDutyCycle(10)
  time.sleep(0.5)
  x.ChangeDutyCycle(12.5)
  y.ChangeDutyCycle(12.5)
  time.sleep(0.5)
  x.ChangeDutyCycle(10)
  y.ChangeDutyCycle(10)
  time.sleep(0.5)
  x.ChangeDutyCycle(7.5)
  y.ChangeDutyCycle(7.5)
  time.sleep(0.5)
  x.ChangeDutyCycle(5)
  y.ChangeDutyCycle(5)
  time.sleep(0.5)
  x.ChangeDutyCycle(2.5)
  y.ChangeDutyCycle(2.5)
  time.sleep(0.5)
