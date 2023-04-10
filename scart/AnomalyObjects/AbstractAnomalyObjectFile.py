import sys

if sys.version_info.major == 3:
    from abc import ABC, abstractclassmethod
    class AbstractAnomalyObject(ABC):
        """
        Abstract base class for anomaly objects.

        Subclasses of this class should implement the detect_anomaly method.

        Attributes:
            Name (str): The name of the anomaly object.
        """
        Name = 'AbstractAnomalyObject'

else:
    from abc import ABCMeta, abstractmethod
    class AbstractAnomalyObject:
        """
        Abstract base class for anomaly objects.

        Subclasses of this class should implement the detect_anomaly method.

        Attributes:
            Name (str): The name of the anomaly object.
        """
        __metaclass__ = ABCMeta
        Name = 'AbstractAnomalyObject'
