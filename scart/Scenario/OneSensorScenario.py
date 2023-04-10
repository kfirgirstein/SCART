#test history and anomalies 
from  .BaseScenario import AbstractScenario,BasicScenarioCallback
import scart.history as history
import threading

class OneSensorScenario(AbstractScenario):  
    Name = 'OneSensorScenario'
    def __init__(self,sensor_name,topic_list,**kwargs):
        import sys
        if sys.version_info.major == 3:
            super().__init__(sensor_name,topic_list,**kwargs)
        else:
            super(OneSensorScenario,self).__init__(sensor_name,topic_list,**kwargs)
        if kwargs:
            self.init_parameters(**kwargs)
    
    def getName(self):
        return self.Name

    def install_scenario(self):
        callbackHolder = BasicScenarioCallback(self.starting_conditions,self.ending_conditions,self.actions)
        callback = callbackHolder.getScenarioCallback()
        self.topic_history.add_sensor(self.sensor_name,callback)

    def listener(self,row):
        if not self.listeners:
            self.listeners = ListenerCtrl.SimpleListener(self.topic_history,self.sensor_name)

        self.listeners.listen(row)

    def init_parameters(self,**parameters):
        self.__dict__.update(parameters)
        












