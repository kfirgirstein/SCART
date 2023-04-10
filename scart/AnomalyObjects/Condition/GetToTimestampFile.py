from .AbstractConditionFile import AbstractCondition

class GetTimestamp(AbstractCondition):
    Name = "GetTimestamp"
    
    def __init__(self,scenario):
        self.topic_history = scenario.topic_history
        self.sensor_name = scenario.sensor_name
        if not 'starting_timestamp' in scenario.__dict__:
            raise KeyError("parameter starting_timestamp is not defined")
        self.starting_timestamp = scenario.starting_timestamp        
        
    def check_condition(self):
        history = self.topic_history.get_sensor_history(self.sensor_name)
        return len(history) > self.starting_timestamp