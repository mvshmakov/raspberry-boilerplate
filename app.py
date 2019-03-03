#!/usr/bin/python3
from flask import Flask
from configparser import ConfigParser
from rightech_client import RightechClient
from os import path, getcwd
from json import dumps

app = Flask(__name__)


SUB_TOPICS = [
    'lighting/green'
]


def message_handler(mqttc, userdata, msg):
    payload = msg.payload.decode("utf-8")
    if msg.topic == SUB_TOPICS[0] and payload == '0':
        print('fucking win!!!!')


@app.route('/<query>')
def index(query):
    mqtt_api_wrapper.mq_client.publish('sensor', dumps(
        {"temp": int(query), "light": 123}
    ))
    return 'data posted'

@app.route('/get_len', methods=['GET'])
def get_len():
    name = request.form['name'];
    return json.dumps({'len': len(name)})


if __name__ == "__main__":
    config_parser = ConfigParser()
    config = path.realpath(path.join(getcwd(), 'api.conf'))
    config_parser.read(config)

    global mqtt_api_wrapper
    mqtt_api_wrapper = RightechClient(
        host=config_parser.get('broker', 'host'),
        port=config_parser.get('broker', 'port'),
        client_id=config_parser.get('credentials', 'client_id'),
        login=config_parser.get('credentials', 'login'),
        password=config_parser.get('credentials', 'password'),
        on_mq_message=message_handler,
        sub_topics=SUB_TOPICS
    )

    # app.debug = True
    app.run(host='0.0.0.0', threaded=True)
