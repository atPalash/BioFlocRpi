import json

from discord_webhook import DiscordWebhook, DiscordEmbed


class DiscordSensor:
    def __init__(self, sensorname, avatar="",
                 url='https://discordapp.com/api/webhooks/708640113269276703'
                     '/RtDV1ZoPKwi440NXYvQkTGUQc0wIg9UVMDJ2UrWRHXQvsEPvGDh2bX31pK4LzGoZ1Drg'):
        self.webhook = DiscordWebhook(url, username=sensorname, avatar_url=avatar)
        self.embed = None

    def addFile(self, fileLocation):
        with open(fileLocation, "rb") as f:
            self.webhook.add_file(file=f.read(), filename=fileLocation)

    def addContent(self, messageIn):
        self.webhook.content = messageIn

    def addEmbed(self, embedTitle, embedMessage):
        # leave this out if you dont want an embed
        # for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
        self.embed = DiscordEmbed(title=embedTitle, description=embedMessage, color=242424)
        self.webhook.add_embed(self.embed)

    def postMessage(self):
        response = self.webhook.execute()


if __name__ == "__main__":
    CameraSensor = DiscordSensor("camera")
    title = "CameraData"
    message = "hello from RPi"
    image = "rpi.jpg"
    file = "testData.txt"
    CameraSensor.addContent(message)
    # CameraSensor.addEmbed(title, message)
    CameraSensor.addFile(image)
    # CameraSensor.addFile(file)
    CameraSensor.postMessage()