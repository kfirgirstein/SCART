from .AbstractConditionFile import AbstractCondition

class EndTime(AbstractCondition):
    Name = "EndTime"
    
    def __init__(self, scenario):
        if not 'duration' in scenario.__dict__:
            raise KeyError("parameter duration is not defined")
        
        self.duration = scenario.duration
    
    def check_condition(self):
        if self.duration > 0:
            self.duration -=  1
            return False

        return True 