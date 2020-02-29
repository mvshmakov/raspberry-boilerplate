#!/usr/bin/python3

from json import dumps

from os import getcwd
from os.path import realpath, join
from time import sleep

from configparser import ConfigParser
from flask import Flask, render_template, make_response

from rightech.client import RightechClient, TOPICS
# from breadboard.controller import BreadboardController
from breadboard.fake_controller import FakeBreadboardController

app = Flask(__name__)

global mqtt_api_wrapper
global breadboard_controller


@app.route('/')
def index():
    return render_template('index.html')


def publish_sensor_data(updated_sensors_data):
    for sensor_name in updated_sensors_data:
        sensor_data = updated_sensors_data[sensor_name]
        mqtt_api_wrapper.mq_client.publish(sensor_data["topic"], dumps(sensor_data["value"]))
        sleep(0.01)


@app.route('/poll_sensors', methods=['GET'])
def poll_sensors():
    updated_sensors_data = breadboard_controller.poll_sensors()

    publish_sensor_data(updated_sensors_data)
    return render_template('sensors.html', sensors=updated_sensors_data)


@app.route('/poll_sensors_manual', methods=['GET'])
def poll_sensors_manual():
    updated_sensors_data = breadboard_controller.poll_sensors_manual()

    publish_sensor_data(updated_sensors_data)
    return render_template('sensors.html', sensors=updated_sensors_data)


@app.route('/switch_button', methods=['GET'])
def switch_button():
    breadboard_controller.switch_button()
    return make_response("<h2>200 OK</h2>", 200)


@app.route('/sync_all', methods=['GET'])
def sync_all():
    updated_sensors_data = breadboard_controller.poll_sensors()
    updated_manual_sensors_data = breadboard_controller.poll_sensors_manual()

    publish_sensor_data(updated_sensors_data)
    publish_sensor_data(updated_manual_sensors_data)

    return make_response("<h2>200 OK</h2>", 200)


def broker_messages_processor(mqttc, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(f"Message from broker received from topic \"{msg.topic}\" with payload: {payload}")

    if msg.topic == TOPICS["switch_button_command"]:
        breadboard_controller.switch_button()
    if msg.topic == TOPICS["poll_sensors_manual_command"]:
        publish_sensor_data(breadboard_controller.poll_sensors_manual())


if __name__ == "__main__":
    config_parser = ConfigParser()
    config = realpath(join(getcwd(), 'api.conf'))
    config_parser.read(config)

    mqtt_api_wrapper = RightechClient(
        host=config_parser.get('broker', 'host'),
        port=config_parser.get('broker', 'port'),
        client_id=config_parser.get('credentials', 'client_id'),
        login=config_parser.get('credentials', 'login'),
        password=config_parser.get('credentials', 'password'),
        on_mq_message=broker_messages_processor,
        sub_topics=TOPICS
    )

    # breadboard_controller = BreadboardController()
    breadboard_controller = FakeBreadboardController()

    app.run(host='0.0.0.0', threaded=True, debug=True, use_reloader=True)
