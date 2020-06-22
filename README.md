# Mohm-lhf

Mohm-lhf is the software that embeddeds the LHF Instrumentação milliohmmeter's.

This software is meant to run at Raspberry pi and as whole project it makes use of:

* LHF Instrumentação ohmmeter's hardware;
* PiPyADC to read analogs input that reads the data in the hardware;
* Pymodbus enabling the raspberry pi work as an assynchronos modbus server;
* PySide2 as a python GUI;

The complete readme will be written as the project evolves, meanwhile the rest of it will keep as the templete standart.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
It will be updated
```

### Usage in a Raspberry Pi

Init de GUI by just running the Program python file.

### Tests in any other OS

In order to avoid the failure by the missing hardware components, in the **measurement** python file, you should: 

Comment the following lines:

* from mohm import OHMIMETRO
* mohm = OHMIMETRO()
* mohm.ADS_Calib()

Change the following lines from:

```
...
resistance = mohm.do_measurement(scale, data_rate, stabilization, aquisitions)
...
...
temperature = mohm.get_temperature()
...
```

 To:
 
 ```
...
resistance = randaom()
...
...
temperature = 20
...
```

And then run the **Program** python file.

## Authors

* **Wuerike Cavalheiro** - *Initial work* - [GitHub](https://github.com/Wuerike)

## License

This project is licensed under the LGPL v2.1 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [PiPyADC](https://github.com/ul-gh/PiPyADC) module
* [Pymodbus](https://github.com/riptideio/pymodbus) modbus stack
