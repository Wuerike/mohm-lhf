# Mohm-lhf

Mohm-lhf is the (in development) software that embeddeds the LHF Instrumentação milliohmmeter's.

This software is meant to run at Raspberry pi and as whole project it makes use of:

* LHF Instrumentação ohmmeter's hardware;
* PiPyADC to read analogs input that reads the data in the hardware;
* Pymodbus enabling the raspberry pi work as an assynchronos modbus server;
* Eel lib to make a GUI by using HTML, CSS and JavaScript as frontend meanwhile python runs at backend;

The complete readme will be written as the project evolves, meanwhile the rest of it will keep as the templete standart.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Wuerike Cavalheiro** - *Initial work* - [GitHub](https://github.com/Wuerike)

See also the list of [contributors](https://github.com/Wuerike/mohm-lhf/graphs/contributors) who participated in this project.

## License

This project is licensed under the LGPL v2.1 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [PiPyADC](https://github.com/ul-gh/PiPyADC) module
* [Eel](https://github.com/samuelhwilliams/Eel) library
* [Pymodbus](https://github.com/riptideio/pymodbus) modbus stack
