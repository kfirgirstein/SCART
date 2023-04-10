## SCART
Simulation of Cyber Attacks for Real-Time Digital Twins

Here you can find the PoC for MiTM threats.
```
├── AnomalyObjects
│   ├── AbstractAnomalyObjectFile.py
│   ├── Action
│   ├── Condition
│   ├── Listener
├── Scenario
│   ├── BaseScenario.py
│   ├── OneSensorScenario.py
│── history.py
├── __init__.py
```

# Installation

```
# from the base folder (AADRT) run:
> python setup.py sdist bdist_wheel
> pip install . #install from current dir

```
And now the usage will be:

```
>>> import scart
>>> from scart import *
>>> dir(scart)
['AnomalyObjects', 'Scenario', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'history']
>>> 

```

## Configuration
This is an example for the configuration for the MiTM

```
{
    "environment" :"CSV",
    "file_path" : "/some/path/to/folder,
    "file_name" : "dataset.csv",
    "sensor_name": "GPS",
    "topic_list": ["lat","lon"],
    "extra_parameters" :{
        "stating_time": 2500,
        "duration" : 5000
    }
}

```