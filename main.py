import RPi.GPIO as GPIO
from time import sleep

#Setup the input ports
led1 = 5
led2 = 6
led3 = 13
in1 = 16
in2 = 20
f = 1 #frequency = 1

#Setup the ports
GPIO.setmode(GPIO.BCM)

#Setup the outputs
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

#Setup the inputs
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Setup the PWM For outputs
pwmLED1 = GPIO.PWM(led1, 1)
pwmLED2 = GPIO.PWM(led2, 1)
pwmLED3 = GPIO.PWM(led3, 1)


def blinkLight(channel):
      channel.start(0)
      for dc in range(101):
        channel.ChangeDutyCycle(dc)
        sleep(.01)

try:
  while True:
    #make the led1 or led2 blink
      
    #LED 1 Blinks
    GPIO.add_event_detect(in1, GPIO.RISING, callback = blinkLight(pwmLED1), bouncetime = 1000)

    #LED 2 Blinks
    GPIO.add_event_detect(in2, GPIO.RISING, callback = blinkLight(pwmLED2), bouncetime = 1000)

    blinkLight(pwmLED3)

    #GPIO Cleanup
except KeyboardInterrupt:
    print('/nExiting')
except Exception as e:
    print('\n'+ e)


pwmLED1.stop()
pwmLED2.stop()
pwmLED3.stop()
GPIO.cleanup()

