import os
from datetime import datetime

from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

os.environ["pubsub_uuid"] = "feerposser-pc"

pnconfig = PNConfiguration()

pnconfig.publish_key = "pub-c-ae306e7e-e4ac-4a15-b231-ab9b76c5c5a0"
pnconfig.subscribe_key = "sub-c-d2a414a2-aba1-11ec-9ae2-de198fffb17e"
pnconfig.uuid = os.environ["pubsub_uuid"]

canal = "imedccso"

pubnub = PubNub(pnconfig)


class RecebeMensagem(SubscribeCallback):
    def presence(self, pubnub, event):
        pass

    def status(self, pubnub, event):
        pass

    def message(self, pubnub, event):
        print("{}: {}\n{}".format(event.message["usr"], event.message["msg"], datetime.now().strftime("%H:%M:%S")))


pubnub.add_listener(RecebeMensagem())
pubnub.subscribe().channels(canal).with_presence().execute()
