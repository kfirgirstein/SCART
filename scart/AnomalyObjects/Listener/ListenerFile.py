from .AbstractListenerFile import AbstractListener

class SimpleListener(AbstractListener):
    """
    A simple listener that saves incoming data to the topic history.

    Args:
        scenario (Scenario): The scenario object that contains the topic history and sensor name.

    Attributes:
        Name (str): The name of the listener ("SimpleListener").

    """

    Name = "SimpleListener"

    def __init__(self, scenario):
        """
        Initializes the SimpleListener.

        Args:
            scenario (Scenario): The scenario object that contains the topic history and sensor name.

        """
        if sys.version_info.major == 3:
            super().__init__(scenario)
        else:
            super(SimpleListener, self).__init__(scenario)
        self.topic_history = scenario.topic_history
        self.sensor_name = scenario.sensor_name

    def listen(self, element):
        """
        Listens to the incoming data and saves it to the topic history.

        Args:
            element: The data to be saved.

        """
        self.topic_history.save(self.sensor_name, element)