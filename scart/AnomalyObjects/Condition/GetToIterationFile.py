from .AbstractConditionFile import AbstractCondition

class GetIteration(AbstractCondition):
    """
    A condition that checks if the length of the sensor history is greater than the starting iteration.

    Attributes:
    - Name (str): The name of the condition
    - topic_history (TopicHistory): The topic history object
    - sensor_name (str): The name of the sensor to check
    - starting_iteration (int): The starting iteration to compare against
    """

    Name = "GetIteration"

    def __init__(self, scenario):
        """
        Initializes the GetIteration object with the given scenario.

        Args:
        - scenario (Scenario): The scenario object containing the necessary parameters
        """
        self.topic_history = scenario.topic_history
        self.sensor_name = scenario.sensor_name
        if not 'starting_iteration' in scenario.__dict__:
            raise KeyError("parameter starting_iteration is not defined")
        self.starting_iteration = scenario.starting_iteration

    def check_condition(self):
        """
        Checks if the length of the sensor history is greater than the starting iteration.

        Returns:
        - bool: True if the condition is met, False otherwise.
        """
        history = self.topic_history.get_sensor_history(self.sensor_name)
        return len(history) > self.starting_iteration