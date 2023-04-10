
import threading
import sys

from  .BaseScenario import AbstractScenario,BasicScenarioCallback
import scart.history as history

class OneSensorScenario(AbstractScenario):  
    """A scenario that monitors a single sensor and triggers actions based on certain conditions.

    Args:
        sensor_name (str): The name of the sensor to monitor.
        topic_list (List[str]): A list of topics to monitor.
        **kwargs: Additional parameters to configure the scenario.

    Attributes:
        Name (str): The name of the scenario.
        starting_conditions (List[Callable[[], bool]]): A list of functions that define the starting conditions for the scenario.
        ending_conditions (List[Callable[[], bool]]): A list of functions that define the ending conditions for the scenario.
        actions (List[Callable[[], None]]): A list of functions that define the actions to take when the scenario is triggered.
        topic_history (history.History): A history object for tracking sensor data.
        listeners (ListenerCtrl.SimpleListener): A listener object for processing sensor data.

    """ 
    Name = 'OneSensorScenario'
    def __init__(self,sensor_name,topic_list,**kwargs):
        """Initializes the OneSensorScenario object.

        Args:
            sensor_name (str): The name of the sensor to monitor.
            topic_list (List[str]): A list of topics to monitor.
            **kwargs: Additional parameters to configure the scenario.

        """
        import sys
        if sys.version_info.major == 3:
            super().__init__(sensor_name,topic_list,**kwargs)
        else:
            super(OneSensorScenario,self).__init__(sensor_name,topic_list,**kwargs)
        if kwargs:
            self.init_parameters(**kwargs)
    
    def getName(self):
        """
        Returns the name of the scenario.

        Returns:
            str: The name of the scenario.

        """
        return self.Name

    def install_scenario(self):
        """
        Installs the scenario by setting up a callback function for the sensor.

        Parameters:
        None

        Returns:
        None
        """
        callbackHolder = BasicScenarioCallback(self.starting_conditions,self.ending_conditions,self.actions)
        callback = callbackHolder.getScenarioCallback()
        self.topic_history.add_sensor(self.sensor_name,callback)

    def listener(self,row):
        """
        Processes sensor data from a listener object.

        Args:
            row: The sensor data to process.

        """
        if not self.listeners:
            self.listeners = ListenerCtrl.SimpleListener(self.topic_history,self.sensor_name)

        self.listeners.listen(row)

    def init_parameters(self,**parameters):
        """
        Initializes additional parameters for the scenario.

        Args:
            **parameters: Additional parameters to configure the scenario.

        """
        self.__dict__.update(parameters)
        












