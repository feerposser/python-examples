import os
from datetime import datetime

from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

os.environ["pubsub_uuid"] = "feerposser"

pnconfig = PNConfiguration()

pnconfig.publish_key = "pub-c-afffceda-e456-4e94-a0cc-b6364eed45e9"
pnconfig.subscribe_key = "sub-c-c0827df5-a7ce-4891-85c1-1777550e00b0"
pnconfig.uuid = os.environ["pubsub_uuid"]

canal = "atitus"

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
