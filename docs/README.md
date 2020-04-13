# Raspberry Digital Oscilloscope

This project is based on the intent to emulate an oscilloscope using a Raspberry Pi, a singleboard computer, and a Signal converter, ADS1115, but later we switched to Yarpie to emulate the signals the program receives by I2C protocol.

To generate scripts write in terminal
```shell
python -m PyQt5.uic.pyuic -x main_frame.ui -o src/view/main_window.py
```
## 1. Description

This program is based on I2C protocol to communicate the SBC with the ADS1115. After the communication is sucessful, the data will be shown at the screen, similar to an oscilloscope, where the user will be able to check the scale, change it if needed, and check the signals the SBC is receiving.

### 1.1 Elements of the Library

* 'OscilloscopeGraphic' - contains the visual implementation of a Oscilloscope screen.
* 'I2CTreatment' - responsible for converting the received data in voltage scale for the oscilloscope.
* 'I2CHandler' - responsible for creating and maintaing the communication via I2C with the conversor.
* 'Observer' - responsible for handling events that may occurs during the application process.

## Usage

## Setup

Execute using Python3.x

* ```pip3 install pygame```
* ```pip3 install PyQt5```

Currently you'll need to install Yarpie emulator on your environment to test it


## How to run

Once dependencies are installed, open src folder and run
in windows
```shell
python .\main.py
```
in linux
```shell
python3 ./main.py
```
