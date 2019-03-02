#!/usr/bin/python3
from time import sleep
import RPi.GPIO as GPIO


# represent as classes
def main():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)  # используем нумерацию GPIO

    GPIO.setup(7, GPIO.OUT)  # конфигурируем GPIO 7 как выход
    GPIO.setup(8, GPIO.IN)  # конфигурируем GPIO 8 как вход

    GPIO.output(7, True)  # выводим на GPIO 7 логическую "1" (3.3 V)
    GPIO.output(7, False)  # выводим на GPIO 7 логический "0"

    # GPIO.add_event_detect(button_pin, GPIO.FALLING,
    #                       callback=self.door_check, bouncetime=1000) 
    # коллбек дёргает ApiWrapper

    # бойлерплейт для цикла
    while True:
        # тело
        signal = GPIO.input(8)  # считываем сигнал с GPIO 8 в переменную signal
        print(signal)

        sleep(3)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  # завершаем работу
