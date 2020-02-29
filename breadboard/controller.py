#!/usr/bin/python3

from time import sleep
from gpiozero import Button, MotionSensor, LED, LightSensor, DistanceSensor, Servo, MCP3008


class BreadboardController:
    """
        Possible GPIO Zero components:
        - Button
        - DistanceSensor
        - LED
        - LightSensor
        - MotionSensor
        - Servo
        - Temperature
    """
    def __init__(self):
        self.switchable_button = Button(1)
        # self.button.when_pressed = Function
        # self.button.when_released = Function
        # self.button.is_pressed

        self.led = LED(2)
        # self.led.source = source
        # self.led.on()
        # self.led.off()
        # self.led.blink()

        self.pir = MotionSensor(3)
        # self.pir.when_motion = Function
        # self.pir.when_no_motion = Function

        self.light_sensor = LightSensor(4)
        # self.light_sensor.when_dark = Function
        # self.light_sensor.when_light = Function
        # self.light_sensor.wait_for_dark()
        # self.light_sensor.wait_for_light()

        self.distance_sensor = DistanceSensor(5, 6)
        # self.distance_sensor = DistanceSensor(5, 6, max_distance=max_distance, threshold_distance=threshold_distance)
        # self.distance_sensor.when_in_range = Function
        # self.distance_sensor.when_out_of_range = Function

        self.servo = Servo(7)
        # self.servo.min()
        # self.servo.mid()
        # self.servo.max()
        # self.servo.source = sin_values()
        # self.servo.source_delay = 0.1

        self.temperature = MCP3008(channel=0)
        # def convert_temp(gen):
        #     for value in gen:
        #         yield (value * 3.3 - 0.5) * 100
        # def play_with_temperature(self):
        #     for temp in self.convert_temp(adc.values):
        #         print('The temperature is', temp, 'C')

    def switch_button(self):
        if self.switchable_button.value == 0:
            self.switchable_button.drive_low()
        else:
            self.switchable_button.drive_high()

    def poll_sensors(self):
        self.switchable_button.play_with_button()
        sleep(0.1)

        self.led.play_with_led()
        self.pir.play_with_pir()
        self.light_sensor.play_with_light_sensor()
        self.distance_sensor.play_with_distance_sensor()
        self.servo.play_with_servo()
        self.temperature.play_with_temperature()

        return {
            "hit": {
                "name": "Hit sensor",
                "value": 231
            },
            "move": {
                "name": "Movement sensor",
                "value": self.pir.value
            },
            "distance": {
                "name": "Distance sensor",
                "value": 231
            },
            "light": {
                "name": "Light sensor",
                "value": 231
            },
            "switchable_button": {
                "name": "Switchable button state",
                "value": self.switchable_button.value
            }
        }

    def poll_sensors_manual(self):
        return {
            "temperature": {
                "id": "temperature",
                "name": "Temperature sensor",
                "value": self.switchable_button.value
            },
            "humidity": {
                "name": "Humidity sensor",
                "value": 231
            }
        }


if __name__ == '__main__':
    breadboard_controller = BreadboardController()

    print(f"Auto-polling data: {breadboard_controller.poll_sensors()}")
    print(f"Manual-polling data: {breadboard_controller.poll_sensors_manual()}")

    breadboard_controller.switch_button()
    print(f"Auto-polling data after button switching: {breadboard_controller.poll_sensors()}")
