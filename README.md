# SCART

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Contributing](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)
[![PyPI version](https://img.shields.io/pypi/v/scart.svg)](https://pypi.org/project/scart/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/kfirgirstein/SCART)](https://github.com/kfirgirstein/SCART/releases)
[![GitHub issues](https://img.shields.io/github/issues/kfirgirstein/SCART.svg)](https://github.com/kfirgirstein/SCART/issues)
[![GitHub forks](https://img.shields.io/github/forks/kfirgirstein/SCART.svg)](https://github.com/kfirgirstein/SCART/network/members)

## Introduction
This repository contains code for the SCART framework, an innovative solution for simulating cyber threats in real-time systems. The SCART framework adds a layer to existing simulators of real-time systems, allowing for the simulation of faults and vulnerabilities. The goal of this framework is to increase the reliability of real-time systems by simulating and testing for possible sensor failures and cyber security attacks. The SCART framework is designed to be modular and extensible, allowing for the addition of new types of faults and vulnerabilities.

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

Instructions for installing the SCART package and its dependencies can be found in the [scart](scart/README.md) folder.

```
# from the base folder (SCART) run:
> python setup.py sdist bdist_wheel
> pip install . #install from current dir
```

## Usage

Instructions for using the SCART package and its various features can be found in the [scart](scart/README.md) folder.

```
>>> import scart
>>> from scart import *
>>> dir(scart)
['AnomalyObjects', 'Scenario', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'history']
>>> 
```
## Contributing

If you wish to contribute to this project, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.


## License

This project is licensed under the [LICENSE](LICENSE) license. A copy of the license can be found in the `LICENSE` file.

## Citation
If you use the SCART framework in your research or project, please cite our paper:

```
@article{girstein2023scart,
      title={SCART: Simulation of Cyber Attacks for Real-Time Digital Twins}, 
      author={Kfir Girstein and Eliron Rahimi and Prof. Avi Mendelson},
      year={2023},
      eprint={2304.03657},
      archivePrefix={arXiv},
      primaryClass={cs.CR}
}

```