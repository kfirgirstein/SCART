from random import SystemRandom
import threading

from .AbstractConditionFile import AbstractCondition


class RandomStart(AbstractCondition):
    """
    A condition that randomly turns off an action based on a given frequency.

    Attributes:
        topic_history (TopicHistory): The topic history to get sensor data from.
        sensor_name (str): The name of the sensor to get data from.
        random_frequency (int): The frequency of randomization. Defaults to 6.
        action_is_on (bool): Flag that indicates whether the action is on or off.
    """

    def __init__(self, scenario):
        """
        Initializes a new instance of the RandomStart class.
        
        :param scenario: The scenario object that contains the topic history and sensor name.
        :type scenario: object
        """
        self.topic_history = scenario.topic_history
        self.sensor_name = scenario.sensor_name
        if not 'frequency' in scenario.__dict__:
            scenario.frequency = 6

        self.random_frequency = scenario.frequency
        self.action_is_on = True
        
    def check_condition(self):
        """
        Checks if the action should be turned off randomly based on the set frequency.
        
        :return: True if the action is on, False otherwise.
        :rtype: bool
        """
        if 1 == SystemRandom().randrange(0,self.random_frequency):
            self.action_is_on = False
        
        return self.action_is_on