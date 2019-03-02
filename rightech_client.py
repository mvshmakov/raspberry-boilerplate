#!/usr/bin/python3
from time import sleep
import paho.mqtt.client as mqtt


class RightechClient:
    def __init__(self, host, port, client_id, login, password,
                 on_mq_message, sub_topics):
        self.host = host
        self.port = port

        self.client_id = client_id
        self.login = login
        self.password = password

        self.sub_topics = sub_topics

        self.on_mq_message = on_mq_message

        self.mq_client = mqtt.Client()
        self._mq_reconnect(force=True)

    def on_mq_connect(self, client, userdata, flags, rc):
        for topic in self.sub_topics:
            self.mq_client.subscribe(topic)

    def _mq_reconnect(self, force=False):
        if force:
            self.mq_connected = False
        while not self.mq_connected:
            try:
                self.mq_client = mqtt.Client(client_id=self.client_id)
                self.mq_client.username_pw_set(
                    self.login, password=self.password
                )

                self.mq_client.on_connect = self.on_mq_connect
                self.mq_client.on_message = self.on_mq_message

                self.mq_client.connect(host=self.host)
                self.mq_client.loop_start()

                self.mq_connected = True
            except Exception as ex:
                print(f'Could not connect to MQ: {ex}')
                sleep(5)
