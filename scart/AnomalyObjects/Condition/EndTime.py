from .AbstractConditionFile import AbstractCondition

class EndTime(AbstractCondition):
    """An anomaly detection condition that ends after a certain duration."""
    Name = "EndTime"
    
    def __init__(self, scenario):
        """Initialize the EndTime condition.

        Args:
            scenario (object): An object containing the duration parameter.
        """
        if not 'duration' in scenario.__dict__:
            raise KeyError("parameter duration is not defined")
        
        self.duration = scenario.duration
    
    def check_condition(self):
        """Check if the condition has been met.

        Returns:
            bool: True if the duration has passed, False otherwise.
        """
        if self.duration > 0:
            self.duration -=  1
            return False

        return True 