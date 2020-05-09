import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin

prev_i = 0
count = 0
while True:
    # i=GPIO.input(12)
    # if i!=prev_i:
    #     print("HEllo", count)
    #     prev_i = i
    #     count += 1
    # time.sleep(0.5)
    count+=1
    if(count == 5):
        message = strftime("Temperature sensor value alert : " + str(count)
        notifier.NotifyAndroid(message)
    if(count == 10):
        message = strftime("Temperature sensor value alert : " + str(count)
        notifier.NotifyAndroid(message)
        break
    time.sleep(0.5)