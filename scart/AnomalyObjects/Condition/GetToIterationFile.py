from .AbstractConditionFile import AbstractCondition

class GetIteration(AbstractCondition):
    Name = "GetIteration"
    
    def __init__(self,scenario):
        self.topic_history = scenario.topic_history
        self.sensor_name = scenario.sensor_name
        if not 'starting_iteration' in scenario.__dict__:
            raise KeyError("parameter starting_iteration is not defined")
        self.starting_iteration = scenario.starting_iteration        
        
    def check_condition(self):
        history = self.topic_history.get_sensor_history(self.sensor_name)
        return len(history) > self.starting_iteration