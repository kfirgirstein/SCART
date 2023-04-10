import sys
if sys.version_info.major == 3:
    from abc import ABC, abstractclassmethod
    class AbstractAnomalyObject(ABC):
        Name = 'AbstractAnomalyObject'
else:
    from abc import ABCMeta, abstractmethod
    class AbstractAnomalyObject:
        __metaclass__ = ABCMeta
        Name = 'AbstractAnomalyObject'
