import time
import random
from DiscordWebhook import DiscordSensor

temperatureSensor = DiscordSensor("TemperatureSensor")
cameraSensor = DiscordSensor("CameraSensor")
count = 0


def start_chat():
    global count
    while True:
        count = random.randint(1, 20)
        if 7<= count <= 10 :
            message = "Temperature sensor value alert : " + str(count)
            temperatureSensor.addContent(message)
            temperatureSensor.postMessage()
        if 15 <= count <= 19:
            message = "Camera sensor value alert : " + str(count)
            cameraSensor.addContent(message)
            image = "raspberry-pi-logo.png"
            cameraSensor.addFile(image)
            cameraSensor.postMessage()
        if count == 20:
            break
    time.sleep(1)
        


if __name__ == "__main__":
    start_chat()
