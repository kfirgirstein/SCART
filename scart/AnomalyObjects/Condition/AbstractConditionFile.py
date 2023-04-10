import sys
from scart.AnomalyObjects import AbstractAnomalyObjectFile

if sys.version_info.major == 3:
    from abc import abstractclassmethod
    class AbstractCondition(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        """Abstract base class for defining conditions to be checked in a scenario.

        Attributes:
        -----------
        Name : str
            A string name for the concrete condition class that will be defined.
        """
        Name = 'AbstractCondition'

        @abstractclassmethod
        def check_condition(self):
            """Abstract method that must be implemented in concrete condition classes.

            This method should define the condition to be checked.
            """
            pass
else:
    from abc import abstractmethod
    class AbstractCondition(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        """Abstract base class for defining conditions to be checked in a scenario.

        Attributes:
        -----------
        Name : str
            A string name for the concrete condition class that will be defined.
        """
        __metaclass__ = ABCMeta
        Name = 'AbstractCondition'

        @abstractmethod
        def check_condition(self):
            """Abstract method that must be implemented in concrete condition classes.

            This method should define the condition to be checked.
            """
            pass