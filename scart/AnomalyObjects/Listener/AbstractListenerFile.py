import sys
from  scart.AnomalyObjects import AbstractAnomalyObjectFile

if sys.version_info.major == 3:
    from abc import abstractclassmethod
    class AbstractListener(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        Name = 'AbstractListener'
    
        def __init__(self,scenario):
            self.topic_history = scenario.topic_history
            self.sensor_name = scenario.sensor_name

        @abstractclassmethod
        def listen(self,element):
            pass
else:
    from abc import abstractmethod
    class AbstractListener(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        Name = 'AbstractListener'
        def __init__(self,scenario):
            self.topic_history = scenario.topic_history
            self.sensor_name = scenario.sensor_name

        @abstractmethod
        def listen(self,element):
            pass


