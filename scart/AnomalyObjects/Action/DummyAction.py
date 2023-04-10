from .AbstractActionFile import AbstractAction


class Dummy(object):
    """
    A dummy class that does nothing when called. Used as a placeholder for some action objects.
    """
    Name = "DummyDuplicateSensor"
    
    def __init__(self, scenario):
        """
        Initializes a new instance of the Dummy class.
        
        :param scenario: The scenario object that contains the topic history and sensor name.
        :type scenario: object
        """
        pass

        
    def do(self):
        """
        Does nothing when called.
        """
        pass
