import scart.history as history
import threading
import sys

if sys.version_info.major == 3:
    from abc import ABC, abstractclassmethod
    class AbstractScenario (ABC):
        Name = 'AbstractScenario'
        def __init__(self,sensor_name,topic_list,**kwargs):
            self.sensor_name = sensor_name
            self.topic_list = topic_list
            self.topic_history =  history.HistoryHolder()
            self.__starting_cond = []
            self.__ending_cond = []
            self.__action_ctrl = []

        @abstractclassmethod
        def getName(self):
            pass

        @property
        def starting_conditions(self):
            return self.__starting_cond
        
        @starting_conditions.setter
        def starting_conditions(self,callback):
            self.__starting_cond.append(callback)

        @property
        def ending_conditions(self):
            return self.__ending_cond
        
        @ending_conditions.setter
        def ending_conditions(self,callback):
            self.__ending_cond.append(callback)

        @property
        def actions(self):
            return self.__action_ctrl
        
        @actions.setter
        def actions(self,callback):
            self.__action_ctrl.append(callback)

        @property
        def listeners(self):
            return self.__listener_ctrl
        
        @listeners.setter
        def listeners(self,callback):
            self.__listener_ctrl = callback
        
        @abstractclassmethod
        def init_parameters(self,**kwargs):
            pass

else:
    from abc import ABCMeta, abstractmethod
    class AbstractScenario():
        __metaclass__ = ABCMeta

        Name = 'AbstractScenario'
        def __init__(self,sensor_name,topic_list,**kwargs):
            self.sensor_name = sensor_name
            self.topic_list = topic_list
            self.topic_history =  history.HistoryHolder()
            self.__starting_cond = []
            self.__ending_cond = []
            self.__action_ctrl = []

        @abstractmethod
        def getName(self):
            pass

        @property
        def starting_conditions(self):
            return self.__starting_cond
        
        @starting_conditions.setter
        def starting_conditions(self,callback):
            self.__starting_cond.append(callback)

        @property
        def ending_conditions(self):
            return self.__ending_cond
        
        @ending_conditions.setter
        def ending_conditions(self,callback):
            self.__ending_cond.append(callback)

        @property
        def actions(self):
            return self.__action_ctrl
        
        @actions.setter
        def actions(self,callback):
            self.__action_ctrl.append(callback)

        @property
        def listeners(self):
            return self.__listener_ctrl
        
        @listeners.setter
        def listeners(self,callback):
            self.__listener_ctrl = callback
        
        @abstractmethod
        def init_parameters(self,**kwargs):
            pass


class BasicScenarioCallback():
    def __init__(self,starting_cond,ending_cond,action_ctrl):
        self.__starting_cond = starting_cond
        self.__ending_cond = ending_cond
        self.__action_ctrl = action_ctrl
        self.is_activate = False

    def getScenarioCallback(self):
        return lambda: self.scenario_callback()
        
    def scenario_callback(self):
        try:
            if not self.is_activate:
                for cond in self.__starting_cond:
                    if not cond.check_condition():
                        return True
                    
            for cond in self.__ending_cond:
                if cond.check_condition():
                    self.is_activate = False
                    return True

            self.is_activate = True
            action_threads = []
            for action in self.__action_ctrl:
                anomaly_thread = threading.Thread(target=action.do)
                anomaly_thread.start()
                action_threads.append(anomaly_thread)

            for action_thread in action_threads:
                action_thread.join()

        except Exception as e:
            print(e)
            print("error in scenario callback")
            return False
        
        return True
        
