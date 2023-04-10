"""
This module provides an abstract class for defining scenarios in a MiTM (Man-in-The-Middle) attack, and a basic scenario callback class.

Classes:
- AbstractScenario: An abstract class for defining scenarios in a MiTM attack. This class defines the interface for defining starting conditions, ending conditions, actions, and listeners for a scenario.
- BasicScenarioCallback: A basic implementation of a scenario callback, which executes the scenario's actions when its starting conditions are met, and stops them when its ending conditions are met.

Functions:
None.

Exceptions:
None.
"""
import scart.history as history
import threading
import sys

if sys.version_info.major == 3:
    from abc import ABC, abstractmethod
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

        @abstractmethod
        def getName(self):

            """
            An abstract method that returns the name of the scenario.

            Parameters:abstractmethod
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

else:
    from abc import ABCMeta, abstractclassmethod
    class AbstractScenario():
        __metaclass__ = ABCMeta
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

            Parameters:
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


class BasicScenarioCallback():
    """
    A class that defines the basic callback for a scenario.

    Attributes:
    - __starting_cond (List[Callable[[], bool]]): A private list of starting conditions callbacks for the scenario.
    - __ending_cond (List[Callable[[], bool]]): A private list of ending conditions callbacks for the scenario.
    - __action_ctrl (List[Callable[[], None]]): A private list of action callbacks for the scenario.
    - is_activate (bool): A flag that indicates whether the scenario is activated or not.

    Methods:
    - getScenarioCallback(): Returns the scenario callback as a lambda function.
    - scenario_callback(): A callback function that checks for starting conditions, ending conditions, and performs the actions.
    """

    def __init__(self,starting_cond,ending_cond,action_ctrl):
        """
        Initializes a new instance of the BasicScenarioCallback class.

        Parameters:
        - starting_cond (List[Callable[[], bool]]): A list of starting conditions callbacks for the scenario.
        - ending_cond (List[Callable[[], bool]]): A list of ending conditions callbacks for the scenario.
        - action_ctrl (List[Callable[[], None]]): A list of action callbacks for the scenario.

        Returns:
        None
        """
        self.__starting_cond = starting_cond
        self.__ending_cond = ending_cond
        self.__action_ctrl = action_ctrl
        self.is_activate = False

    def getScenarioCallback(self):
        """
        Returns the scenario callback as a lambda function.

        Parameters:
        None.

        Returns:
        The scenario callback as a lambda function.
        """
        return lambda: self.scenario_callback()

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

    @property
    def actions(self):
        """
        Setter for the list of action control objects associated with the scenario
        
        Parameters:
        - callback: A function that represents an action.
        
        Returns:
        None.
        """
        return self.__action_ctrl

    def scenario_callback(self):
        """
        A callback function that checks for starting conditions, ending conditions, and performs the actions.

        Parameters:
        None.

        Returns:
        A boolean value indicating whether the scenario callback succeeded or not.
        """
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
        
