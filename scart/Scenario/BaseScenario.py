import scart.history as history
import threading
import sys

if sys.version_info.major == 3:
    from abc import ABC, abstractclassmethod
    class AbstractScenario (ABC):
        """
        An abstract class for defining scenarios in a MiTM attack.
        Attributes:
        - Name (str): The name of the scenario.
        - sensor_name (str): The name of the sensor to which the scenario is attached.
        - topic_list (list): A list of topics that the scenario listens to.
        - topic_history (HistoryHolder): An object that stores the history of the topic messages.
        - __starting_cond (list): A private list of starting conditions callbacks for the scenario.
        - __ending_cond (list): A private list of ending conditions callbacks for the scenario.
        - __action_ctrl (list): A private list of action callbacks for the scenario.
        - __listener_ctrl (function): A private function that listens to messages on the topic list.

        Methods:
        - getName(): An abstract method that returns the name of the scenario.
        - init_parameters(**kwargs): An abstract method that initializes the parameters of the scenario.
        """
        Name = 'AbstractScenario'
        def __init__(self,sensor_name,topic_list,**kwargs):
            """
            Initializes a new instance of the AbstractScenario class.

            Parameters:
            - sensor_name (str): The name of the sensor to which the scenario is attached.
            - topic_list (list): A list of topics that the scenario listens to.
            - **kwargs: Additional parameters to initialize the scenario.

            Returns:
            None.
            """
            self.sensor_name = sensor_name
            self.topic_list = topic_list
            self.topic_history =  history.HistoryHolder()
            self.__starting_cond = []
            self.__ending_cond = []
            self.__action_ctrl = []

        @abstractclassmethod
        def getName(self):

            """
            An abstract method that returns the name of the scenario.

            Parameters:abstractmethod
            None.

            Returns:
            The name of the scenario.
            """
            pass

        @abstractclassmethod
        def install_scenario(self):
            """
            An abstract method that installs the scenario.

            Parameters:
            None.

            Returns:
            None.
            """
            pass
        
        @property
        def starting_conditions(self):
            """
            A property that returns the starting conditions callbacks for the scenario.

            Parameters:
            None.

            Returns:
            A list of starting conditions callbacks for the scenario.
            """
            return self.__starting_cond
        
        @starting_conditions.setter
        def starting_conditions(self,callback):
            """
            A setter method that adds a starting condition callback to the scenario.

            :param: callback (function): A function that checks if the starting condition is met.

            Returns:
            None.
            """
            self.__starting_cond.append(callback)

        @property
        def ending_conditions(self):
            """
            A property that returns the ending conditions callbacks for the scenario.

            Parameters:
            None.

            Returns:
            A list of ending conditions callbacks for the scenario.
            """
            return self.__ending_cond
        
        @ending_conditions.setter
        def ending_conditions(self,callback):
            """
            A property setter that adds an ending condition to the list.

            Parameters:
            - callback: A function that represents an ending condition.
            
            Returns:
            None.

            """
            self.__ending_cond.append(callback)

        @property
        def actions(self):
            """
            A property that returns the action callbacks for the scenario.

            Parameters:
            None.

            Returns:
            A list of action callbacks for the scenario.
            """
            return self.__action_ctrl
        
        @actions.setter
        def actions(self,callback):
            """
            Setter for the list of action control objects associated with the scenario.
            Parameters:
            - callback: A function that represents an action.

            Returns:
            None.

            """
            self.__action_ctrl.append(callback)

        @property
        def listeners(self):
            """
            A property that returns the listener callback for the scenario.

            Parameters:
            None.

            Returns:
            A function that represents the listener callback for the scenario.
            """
            return self.__listener_ctrl
        
        @listeners.setter
        def listeners(self,callback):
            """
            Setter for the listener callback associated with the scenario.

            Parameters:
            - callback: A function that represents the listener callback.

            Returns:
            None.
            """
            self.__listener_ctrl = callback
        
        @abstractclassmethod
        def init_parameters(self,**kwargs):
            """
            An abstract method that initializes the parameters of the scenario.

            Parameters:
            - **kwargs: Additional parameters to initialize the scenario.

            Returns:
            None.
            """
            pass

else:
    from abc import ABCMeta, abstractmethod
    class AbstractScenario():
        """
        An abstract class for defining scenarios in a MiTM attack.
        Attributes:
        - Name (str): The name of the scenario.
        - sensor_name (str): The name of the sensor to which the scenario is attached.
        - topic_list (list): A list of topics that the scenario listens to.
        - topic_history (HistoryHolder): An object that stores the history of the topic messages.
        - __starting_cond (list): A private list of starting conditions callbacks for the scenario.
        - __ending_cond (list): A private list of ending conditions callbacks for the scenario.
        - __action_ctrl (list): A private list of action callbacks for the scenario.
        - __listener_ctrl (function): A private function that listens to messages on the topic list.

        Methods:
        - getName(): An abstract method that returns the name of the scenario.
        - init_parameters(**kwargs): An abstract method that initializes the parameters of the scenario.
        """
        __metaclass__ = ABCMeta
        Name = 'AbstractScenario'
        def __init__(self,sensor_name,topic_list,**kwargs):
            """
            Initializes a new instance of the AbstractScenario class.

            Parameters:
            - sensor_name (str): The name of the sensor to which the scenario is attached.
            - topic_list (list): A list of topics that the scenario listens to.
            - **kwargs: Additional parameters to initialize the scenario.

            Returns:
            None.
            """
            self.sensor_name = sensor_name
            self.topic_list = topic_list
            self.topic_history =  history.HistoryHolder()
            self.__starting_cond = []
            self.__ending_cond = []
            self.__action_ctrl = []

        @abstractmethod
        def getName(self):

            """
            An abstract method that returns the name of the scenario.

            Parameters:
            None.

            Returns:
            The name of the scenario.
            """
            pass

        @abstractmethod
        def install_scenario(self):
            """
            An abstract method that installs the scenario.

            Parameters:
            None.

            Returns:
            None.
            """
            pass
        
        @property
        def starting_conditions(self):
            """
            A property that returns the starting conditions callbacks for the scenario.

            Parameters:
            None.

            Returns:
            A list of starting conditions callbacks for the scenario.
            """
            return self.__starting_cond
        
        @starting_conditions.setter
        def starting_conditions(self,callback):
            """
            A setter method that adds a starting condition callback to the scenario.

            :param: callback (function): A function that checks if the starting condition is met.

            Returns:
            None.
            """
            self.__starting_cond.append(callback)

        @property
        def ending_conditions(self):
            """
            A property that returns the ending conditions callbacks for the scenario.

            Parameters:
            None.

            Returns:
            A list of ending conditions callbacks for the scenario.
            """
            return self.__ending_cond
        
        @ending_conditions.setter
        def ending_conditions(self,callback):
            """
            A property setter that adds an ending condition to the list.

            Parameters:
            - callback: A function that represents an ending condition.
            
            Returns:
            None.

            """
            self.__ending_cond.append(callback)

        @property
        def actions(self):
            """
            A property that returns the action callbacks for the scenario.

            Parameters:
            None.

            Returns:
            A list of action callbacks for the scenario.
            """
            return self.__action_ctrl
        
        @actions.setter
        def actions(self,callback):
            """
            Setter for the list of action control objects associated with the scenario.
            Parameters:
            - callback: A function that represents an action.

            Returns:
            None.

            """
            self.__action_ctrl.append(callback)

        @property
        def listeners(self):
            """
            A property that returns the listener callback for the scenario.

            Parameters:
            None.

            Returns:
            A function that represents the listener callback for the scenario.
            """
            return self.__listener_ctrl
        
        @listeners.setter
        def listeners(self,callback):
            """
            Setter for the listener callback associated with the scenario.

            Parameters:
            - callback: A function that represents the listener callback.

            Returns:
            None.
            """
            self.__listener_ctrl = callback
        
        @abstractmethod
        def init_parameters(self,**kwargs):
            """
            An abstract method that initializes the parameters of the scenario.

            Parameters:
            - **kwargs: Additional parameters to initialize the scenario.

            Returns:
            None.
            """
            pass
