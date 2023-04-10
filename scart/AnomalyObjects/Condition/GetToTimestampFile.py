from .AbstractConditionFile import AbstractCondition

class GetTimestamp(AbstractCondition):
    """
    This class represents a condition that checks if the number of elements in the topic history 
    for a given sensor has exceeded a certain starting timestamp.
    """
    Name = "GetTimestamp"
    
    def __init__(self, scenario):
        """
        Initializes a new instance of the GetTimestamp class.
        
        :param scenario: The scenario object that contains the topic history and sensor name.
        :type scenario: object
        """
        self.topic_history = scenario.topic_history
        self.sensor_name = scenario.sensor_name
        if not 'starting_timestamp' in scenario.__dict__:
            raise KeyError("parameter starting_timestamp is not defined")
        self.starting_timestamp = scenario.starting_timestamp        
        
    def check_condition(self):
        """
        Checks if the number of elements in the topic history for the sensor has exceeded 
        the starting timestamp.
        
        :return: True if the number of elements has exceeded the starting timestamp, False otherwise.
        :rtype: bool
        """
        history = self.topic_history.get_sensor_history(self.sensor_name)
        return len(history) > self.starting_timestamp