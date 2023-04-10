import sys
from scart.AnomalyObjects import AbstractAnomalyObjectFile

# Check if running on Python 3 or later
if sys.version_info.major == 3:
    from abc import abstractclassmethod
    class AbstractListener(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        """
        Abstract base class for listener objects that can be used to detect anomalies
        in a stream of data.

        Attributes:
            Name (str): The name of the listener class.
            topic_history (dict): A dictionary containing the history of topics that
                have been observed by the listener.
            sensor_name (str): The name of the sensor associated with the listener.
        """
        Name = 'AbstractListener'

        def __init__(self, scenario):
            """
            Constructor for AbstractListener.

            Args:
                scenario (Scenario): The scenario object containing information about
                    the sensor and topics being monitored.
            """
            self.topic_history = scenario.topic_history
            self.sensor_name = scenario.sensor_name

        @abstractclassmethod
        def listen(self, element):
            """
            Abstract method that must be implemented by concrete listener classes to
            process incoming data and detect anomalies.

            Args:
                element (dict): A dictionary containing data from a single topic
                    observation.

            Returns:
                None
            """
            pass
else:
    from abc import abstractmethod
    class AbstractListener(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        """
        Abstract base class for listener objects that can be used to detect anomalies
        in a stream of data.

        Attributes:
            Name (str): The name of the listener class.
            topic_history (dict): A dictionary containing the history of topics that
                have been observed by the listener.
            sensor_name (str): The name of the sensor associated with the listener.
        """
        __metaclass__ = ABCMeta
        Name = 'AbstractListener'

        def __init__(self, scenario):
            """
            Constructor for AbstractListener.

            Args:
                scenario (Scenario): The scenario object containing information about
                    the sensor and topics being monitored.
            """
            self.topic_history = scenario.topic_history
            self.sensor_name = scenario.sensor_name

        @abstractmethod
        def listen(self, element):
            """
            Abstract method that must be implemented by concrete listener classes to
            process incoming data and detect anomalies.

            Args:
                element (dict): A dictionary containing data from a single topic
                    observation.

            Returns:
                None
            """
            pass