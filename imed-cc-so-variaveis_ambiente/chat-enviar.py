import os

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

os.environ["pubsub_uuid"] = "feerposser-pc"

pnconfig = PNConfiguration()

pnconfig.publish_key = "pub-c-ae306e7e-e4ac-4a15-b231-ab9b76c5c5a0"
pnconfig.subscribe_key = "sub-c-d2a414a2-aba1-11ec-9ae2-de198fffb17e"

pnconfig.uuid = os.environ["pubsub_uuid"]

# pnconfig.publish_key = os.getenv("pubsub_pub")
# pnconfig.subscribe_key = os.getenv("pubsub_sub")

# set pubsub_pub=pub-c-18a9fb37-6f1b-4217-992b-fa9ec609c206
# set pubsub_sub=sub-c-af1bcac4-11b5-11ec-83e9-0e85f81976b6

canal = "imedccso"

usr = input("Seu nome: ")
print("-"*50)

pubnub = PubNub(pnconfig)

while True:
    msg = input("Fala ae: ")
    envelope = pubnub.publish().channel(canal).message({"msg": msg, "usr": usr}).sync()

    if envelope.status.is_error():
        print("->>>>> DEU PAU")
