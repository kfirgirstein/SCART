from .AbstractActionFile import AbstractAction

class DisconnectSensor(AbstractAction):
    """
    An action that disconnects a sensor by setting its value to a specified disconnect value.

    :param scenario: The scenario object that contains the topic history and sensor name.
    :type scenario: object
    """
    Name = "DisconnectSensor"

    def __init__(self, scenario):
        self.topic_history = scenario.topic_history
        self.sensor_name = scenario.sensor_name
        self.topic_list = scenario.topic_list

        # If disconnect_value is not defined, set it to -1
        if not hasattr(scenario, "disconnect_value"):
            scenario.disconnect_value = -1

        self.disconnect_value = scenario.disconnect_value

    def do(self):
        """
        Disconnects the sensor by setting its value to the disconnect value.
        """
        sensor_history = self.topic_history.get_sensor_history(self.sensor_name)
        history_lst = sensor_history.history

        if len(history_lst) < 1:
            return

        last_record = sensor_history.top()
        if type(last_record) is dict:
            for sensor in self.topic_list:
                history_lst[-1][sensor] = self.disconnect_value
        else:
            for sensor in self.topic_list:
                setattr(history_lst[-1], sensor, self.disconnect_value)
