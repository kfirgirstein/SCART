
class History(object):
    """
    Represents a history object which stores a list of events and supports adding observers
    to be notified when new events are added to the history.

    A class for storing historical data and notifying observers of changes.
    """
    def __init__(self, name, on_change=None):
        """
        Initializes a new instance of the History class.

        :param name: The name of the history object.
        :type name: str
        :param on_change: A function or list of functions to be called when the history changes.
        :type on_change: callable or list of callable
        """
        self.__observer__ = on_change
        self.__name__ = name
        self.__history__ = []

    def __len__(self):
        """
        Returns the number of items in the history.

        :return: The number of items in the history.
        :rtype: int
        """
        return len(self.__history__)

    def tail(self):
        """
        Returns the last item added to the history.

        :return: The last item added to the history.
        :rtype: object or None
        """
        return self.__history__[0] if self.__history__ and len(self.__history__) > 0 else None

    def top(self):
        """
        Returns the most recently added item to the history.

        :return: The most recently added item to the history.
        :rtype: object or None
        """
        return self.__history__[-1] if self.__history__ and len(self.__history__) > 0 else None

    def observer_get(self):
        """
        Returns the function or list of functions to be called when the history changes.

        :return: The function or list of functions to be called when the history changes.
        :rtype: callable or list of callable
        """
        return self.__observer__

    def observer_set(self, on_change):
        """
        Sets the function or list of functions to be called when the history changes.

        :param on_change: A function or list of functions to be called when the history changes.
        :type on_change: callable or list of callable
        """
        if type(on_change) is list:
            self.__observer__.extend(on_change)
        else:
            self.__observer__ = on_change

    observer = property(observer_get, observer_set)

    def history_get(self):
        """
        Returns the list of items in the history.

        :return: The list of items in the history.
        :rtype: list of object
        """
        return self.__history__

    def history_set(self, new):
        """
        Adds a new item to the history and calls the observer function(s).

        :param new: The new item to add to the history.
        :type new: object
        """
        self.__history__.append(new)
        if self.observer:
            if type(self.observer) is list:
                for f in self.observer:
                    success = f()
                    if not success:
                        break
            else:
                self.observer()

    history = property(history_get, history_set)

    def name_get(self):
        """
        Returns the name of the history object.

        :return: The name of the history object.
        :rtype: str
        """
        return self.__name__

    name = property(name_get)

class HistoryHolder(object):
    """
    A class for managing multiple sensors' histories.
    """

    def __init__(self):
        """
        Initializes a new instance of the HistoryHolder class.
        """
        self._sensors = {}

    def add_sensor(self, sensor_name, on_change):
        """
        Adds a new sensor to the history holder.

        Args:
        - sensor_name: A string representing the name of the sensor.
        - on_change: A function or list of functions to be called whenever the sensor's history is updated.
        """
        if sensor_name in self._sensors:
            if type(self._sensors[sensor_name]) is not History:
                raise Exception("Sensor type initialized without history")
            self._sensors[sensor_name].observer = on_change
        else:
            self._sensors[sensor_name] = History(sensor_name, on_change)

    def save(self, sensor_name, data):
        """
        Saves new data for a given sensor.

        Args:
        - sensor_name: A string representing the name of the sensor.
        - data: The data to be saved.
        """
        if not sensor_name in self._sensors:
            raise Exception("Sensor name " + sensor_name + " is not in History")

        self._sensors[sensor_name].history = data

    def get_sensor_history(self, sensor_name):
        """
        Gets the history for a given sensor.

        Args:
        - sensor_name: A string representing the name of the sensor.

        Returns:
        A History object representing the sensor's history.
        """
        if not sensor_name in self._sensors:
            raise Exception("Sensor name " + sensor_name + " is not in History")

        return self._sensors[sensor_name]
            