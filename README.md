# raspberry-boilerplate
##### Consider it exactly as a boilerplate, not as the library!
##### That means you can change every file existing in the repo to fit your needs.

## Running in the virtualenv:
##### 1) Install `virtualenv`:
* `~ python3 -m pip install virtualenv`
##### 2) Create virtual environment:
* `~ python3 -m venv env`
##### 3) Activate virtual environment:
* `~ source env/bin/activate`
##### 4) Install dependencies:
* `~ pip3 install --upgrade pip` (if needed)
* `~ pip3 install -r requirements.txt`
##### 5) If you are working under the MacOS environment, `RPi.GPIO` is not available. 
##### For MacOS install `FakeRPi`, in other OS install `RPi.GPIO`:
* `~ pip3 install git+https://github.com/sn4k3/FakeRPi` (for MacOS)
* `~ pip3 install RPi.GPIO` (for other)
##### 6) Running the app in development mode (with "watch mode"):
* `~ FLASK_APP=app.py FLASK_ENV=development python -m flask run`
##### 7) In order to exit from venv:
* `~ deactivate`

## Installing `Raspbian Stretch` (Raspberry OS): https://romantelychko.com/blog/1611/

## Working with `GPIO`:
#### 1) http://hexvolt.blogspot.com/2013/02/raspberry-pi-gpio.html

## Working with `RFID`:
#### 1) https://pimylifeup.com/raspberry-pi-rfid-rc522/
#### 2) https://www.raspberrypi-spy.co.uk/2018/02/rc522-rfid-tag-read-raspberry-pi/

## Working with a `temperature` and `humidity` sensor:
#### 1) https://kropochev.com/?go=all%2Fraspberry-pi-and-humidity-sensor-dht%2F
#### 2) https://www.rlocman.ru/review/article.html?di=336425
#### 3) https://sysengineer.ru/2018/10/27/schityvanie-dannyh-s-datchika-vlazhnosti-i-temperatury-dht11-na-orange-pi-pri-pomoschi-python-3.html

## Working with `LCD`:
#### 1) [https://masterkit.ru/zip/raspi-dht11-i2clcd.py](https://www.rlocman.ru/review/article.html?di=336425)
#### 2) http://www.circuitbasics.com/raspberry-pi-lcd-set-up-and-programming-in-python/

## GPIO Zero library recipes with Pin Numbering:
#### https://gpiozero.readthedocs.io/en/stable/recipes.html

## Example:
#### https://github.com/gurumitts/garage-butler/blob/master/garage/butler.py

# If not Raspberry PI:

## Arduino docs and samples:
#### https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.04-Reading-a-Sensor-with-Python/
#### https://forum.arduino.cc/index.php?topic=463101.0
#### https://pypi.org/project/pyFirmata/
#### https://gist.github.com/otknoy/df167c6f5f8b265b3e65
#### !! https://alexgyver.ru/lessons/serial/
#### Setup of serial port for communicating with python: https://www.instructables.com/id/How-to-Communicate-With-Arduino-From-a-Python-Scri/
#### Library fotr communicating: https://github.com/thearn/Python-Arduino-Command-API
#### A lot of examples: https://yandex.ru/search/?text=communicating%20with%20arduino%20from%20local%20python&lr=213&clid=1955453&win=345
