from .AbstractScenarioCallback import AbstractScenarioCallback
import threading


class BasicScenarioCallback(AbstractScenarioCallback):
    """
    A class that defines the basic callback for a scenario.

    Attributes:
    - __starting_cond (List[Callable[[], bool]]): A private list of starting conditions callbacks for the scenario.
    - __ending_cond (List[Callable[[], bool]]): A private list of ending conditions callbacks for the scenario.
    - __action_ctrl (List[Callable[[], None]]): A private list of action callbacks for the scenario.
    - is_activate (bool): A flag that indicates whether the scenario is activated or not.

    Methods:
    - get_scenario_callback(): Returns the scenario callback as a lambda function.
    - scenario_callback(): A callback function that checks for starting conditions, ending conditions, and performs the actions.
    """

    Name = 'BasicScenarioCallback'

    def __init__(self, starting_cond, ending_cond, action_ctrl):
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
