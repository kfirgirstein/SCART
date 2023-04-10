import sys
from  scart.AnomalyObjects import AbstractAnomalyObjectFile

if sys.version_info.major == 3:
    from abc import abstractclassmethod
    class AbstractCondition(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        Name = 'AbstractCondition'
    
        @abstractclassmethod
        def check_condition():
            pass
else:
    from abc import abstractmethod
    class AbstractCondition(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        Name = 'AbstractCondition'
    
        @abstractmethod
        def check_condition():
            pass


