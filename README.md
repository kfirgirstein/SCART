# SCART

[![Build Status](https://travis-ci.org/your_username/your_repo.svg?branch=master)](https://travis-ci.org/your_username/your_repo)
[![Coverage Status](https://coveralls.io/repos/github/your_username/your_repo/badge.svg?branch=master)](https://coveralls.io/github/your_username/your_repo?branch=master)

## Introduction
This repository contains code for the SCART framework, an innovative solution for simulating cyber threats in real-time systems. The SCART framework adds a layer to existing simulators of real-time systems, allowing for the simulation of faults and vulnerabilities. The goal of this framework is to increase the reliability of real-time systems by simulating and testing for possible sensor failures and cyber security attacks. The SCART framework is designed to be modular and extensible, allowing for the addition of new types of faults and vulnerabilities. The SCART framework is currently being used to test the resilience of the [AUVSI SUAS Competition](https://www.auvsi-suas.org/).

Here you can find the PoC for MiTM threats.
```
├── AnomalyObjects
│   ├── AbstractAnomalyObjectFile.py
│   ├── Action
│   ├── Condition
│   ├── Listener
├── Scenario
│   ├── BaseScenario.py
│   ├── OneSensorScenario.py
│── history.py
├── __init__.py
```

## Installation

Instructions for installing the SCART package and its dependencies can be found in the [MiTM](MiTM/README.md) folder.

```
# from the base folder (AADRT) run:
> python setup.py sdist bdist_wheel
> pip install . #install from current dir
```

## Usage

Instructions for using the SCART package and its various features can be found in the [MiTM](MiTM/README.md) folder.

```
>>> import MiTM
>>> from MiTM import *
>>> dir(MiTM)
['AnomalyObjects', 'Scenario', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'history']
>>> 
```
## Contributing

If you wish to contribute to this project, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.


## License

This project is licensed under the [LICENSE](LICENSE) license. A copy of the license can be found in the `LICENSE` file.
