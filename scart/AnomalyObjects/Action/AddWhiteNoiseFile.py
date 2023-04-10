from random import SystemRandom
from .AbstractActionFile import AbstractAction
import numpy as np


class AddWhiteNoise(AbstractAction):
    """
    An action that adds white noise to a sensor's history in a scenario.
    """

    Name = "AddWhiteNoise"

    def __init__(self, scenario):
        """
        Initializes a new instance of the AddWhiteNoise class.

        :param scenario: The scenario object that contains the topic history, sensor name, topic list, sigma and mu.
        :type scenario: object
        """
        self.topic_history = scenario.topic_history
        self.sensor_name = scenario.sensor_name
        self.topic_list = scenario.topic_list
        np.random.seed(SystemRandom().randrange(0, 2 ** 32 - 1))

        if not hasattr(scenario, "sigma"):
            scenario.sigma = 0.1
        if not hasattr(scenario, "mu"):
            scenario.mu = 0

        self.sigma = scenario.sigma
        self.mu = scenario.mu

    def do(self):
        """
        Adds white noise to the sensor's history in the scenario.
        """
        sensor_history = self.topic_history.get_sensor_history(self.sensor_name)
        history_lst = sensor_history.history

        # Randomly select a topic to change
        if len(history_lst) < 1:
            return

        last_record = sensor_history.top()

        for sensor in self.topic_list:
            if type(history_lst[-1]) is dict:
                history_lst[-1][sensor] = history_lst[-1][sensor] + np.random.normal(self.mu, self.sigma)
            else:
                if not hasattr(last_record, sensor):
                    raise KeyError("topic " + str(sensor) + " is not defined in " + str(type(last_record)))
                setattr(last_record, sensor, getattr(last_record, sensor) + np.random.normal(self.mu, self.sigma))
