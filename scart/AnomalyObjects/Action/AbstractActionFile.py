import sys
from  scart.AnomalyObjects import AbstractAnomalyObjectFile

if sys.version_info.major == 3:
    from abc import abstractclassmethod
    class AbstractAction(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        Name = 'AbstractAction'
        
        @abstractclassmethod
        def do():
            pass
else:
    from abc import abstractmethod
    class AbstractAction(AbstractAnomalyObjectFile.AbstractAnomalyObject):
        Name = 'AbstractAction'
        
        @abstractmethod
        def do():
            pass





