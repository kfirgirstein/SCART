import sys

if sys.version_info.major == 3:
    from abc import ABC, abstractclassmethod
    class AbstractScenarioCallback(ABC):
        Name = 'AbstractScenarioCallback'
        
        def get_scenario_callback(self):
            """
            Returns the scenario callback as a lambda function.

            Returns:
            The scenario callback as a lambda function.
            """
            return lambda: self.scenario_callback()

        @property
        def starting_conditions(self):
            """
            A property that returns the starting conditions callbacks for the scenario.

            Returns:
            A list of starting conditions callbacks for the scenario.
            """
            return self._starting_cond

        @property
        def ending_conditions(self):
            """
            A property that returns the ending conditions callbacks for the scenario.

            Returns:
            A list of ending conditions callbacks for the scenario.
            """
            return self._ending_cond

        @property
        def actions(self):
            """
            Setter for the list of action control objects associated with the scenario.

            Returns:
            The list of action control objects associated with the scenario.
            """
            return self._action_ctrl

        @abstractclassmethod
        def scenario_callback(self):
            """
            A callback function that checks for starting conditions, ending conditions, and performs the actions.

            Returns:
            A boolean value indicating whether the scenario callback succeeded or not.
            """
            pass
            
else:
    from abc import ABCMeta, abstractmethod
    class AbstractScenarioCallback(object):
        __metaclass__ = ABCMeta
        Name = 'AbstractScenarioCallback'
        
        def get_scenario_callback(self):
            """
            Returns the scenario callback as a lambda function.

            Returns:
            The scenario callback as a lambda function.
            """
            return lambda: self.scenario_callback()

        @property
        def starting_conditions(self):
            """
            A property that returns the starting conditions callbacks for the scenario.

            Returns:
            A list of starting conditions callbacks for the scenario.
            """
            return self._starting_cond

        @property
        def ending_conditions(self):
            """
            A property that returns the ending conditions callbacks for the scenario.

            Returns:
            A list of ending conditions callbacks for the scenario.
            """
            return self._ending_cond

        @property
        def actions(self):
            """
            Setter for the list of action control objects associated with the scenario.

            Returns:
            The list of action control objects associated with the scenario.
            """
            return self._action_ctrl

        @abstractmethod
        def scenario_callback(self):
            """
            A callback function that checks for starting conditions, ending conditions, and performs the actions.

            Returns:
            A boolean value indicating whether the scenario callback succeeded or not.
            """
            pass
