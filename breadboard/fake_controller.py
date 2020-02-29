from random import random
from time import sleep

from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Button, LED, MotionSensor

from rightech.client import TOPICS

Device.pin_factory = MockFactory()


def get_random_value():
    return float('{:.2f}'.format(random())) * 100


class FakeBreadboardController:
    def __init__(self):
        self.button = Button(16)
        self.led = LED(17)
        self.sensor = MotionSensor(18)
        self.switchable_button = Button(19)

        self.led.source = self.button

        # Get a reference to mock pin 16 (used by the button)
        self.btn_pin = Device.pin_factory.pin(16)
        self.motion_pin = Device.pin_factory.pin(18)
        self.switch_btn_pin = Device.pin_factory.pin(19)

    def switch_button(self):
        if self.switchable_button.value == 0:
            self.switch_btn_pin.drive_low()
        else:
            self.switch_btn_pin.drive_high()

    def poll_sensors(self):
        # Drive the pin low (this is what would happen electrically when the button is
        # pushed)
        if self.led.value == 0:
            self.btn_pin.drive_low()
            sleep(0.1)  # give source some time to re-read the button state
        else:
            self.btn_pin.drive_high()
            sleep(0.1)

        #####

        if not self.sensor.motion_detected:
            self.motion_pin.drive_high()
            sleep(0.1)  # give source some time to re-read the button state
        else:
            self.motion_pin.drive_low()
            sleep(0.1)

        return {
            "hit": {
                "name": "Hit sensor",
                "topic": TOPICS["hit_data"],
                "value": get_random_value()
            },
            "move": {
                "name": "Movement sensor",
                "topic": TOPICS["move_data"],
                "value": self.sensor.motion_detected
            },
            "distance": {
                "name": "Distance sensor",
                "topic": TOPICS["distance_data"],
                "value": get_random_value()
            },
            "light": {
                "name": "Light sensor",
                "topic": TOPICS["light_data"],
                "value": get_random_value()
            },
            "switchable_button": {
                "name": "Switchable button state",
                "topic": TOPICS["switchable_button_data"],
                "value": self.switchable_button.value
            }
        }

    def poll_sensors_manual(self):
        return {
            "temperature": {
                "name": "Temperature sensor",
                "topic": TOPICS["temperature_data"],
                "value": int(self.button.value) + 7
            },
            "humidity": {
                "name": "Humidity sensor",
                "topic": TOPICS["humidity_data"],
                "value": get_random_value()
            }
        }


if __name__ == '__main__':
    breadboard_controller = FakeBreadboardController()

    print(f"Auto-polling data: {breadboard_controller.poll_sensors()}")
    print(f"Manual-polling data: {breadboard_controller.poll_sensors_manual()}")

    breadboard_controller.switch_button()
    print(f"Auto-polling data after button switching: {breadboard_controller.poll_sensors()}")
