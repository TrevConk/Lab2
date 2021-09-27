import RPi.GPIO as GPIO
from time import sleep
from functools import partial

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


#Setup the inputs
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Setup the PWM For outputs

pwmLED2 = GPIO.PWM(led2, 100)
pwmLED3 = GPIO.PWM(led3, 100)


try:

  def blinkLight(channel):
      GPIO.setup(led1, GPIO.OUT)
      pwmLED = GPIO.PWM(led1, 100)
      pwmLED.start(0)
      for dc in range(101):
        pwmLED.ChangeDutyCycle(dc)
        sleep(.01)
      pwmLED.stop()

    #make the led1 or led2 blink
      
    #LED 1 Blinks
  #GPIO.add_event_detect(in1, GPIO.RISING, callback = partial(blinkLight, pwmLED1), bouncetime = 1000)
    #LED 2 Blinks
  #GPIO.add_event_detect(in2, GPIO.RISING, callback = partial(blinkLight, pwmLED2), bouncetime = 1000)

  while True:
    blinkLight(led3)
    print('blinking')

    #GPIO Cleanup
except KeyboardInterrupt:
    print('/nExiting')
except Exception as e:
    print('\n',e)

GPIO.cleanup()

