from .AbstractActionFile import AbstractAction

class AvgSensors(AbstractAction):
    """
    Updates the first topic in the topic list to the average of all topic values.
    """
    Name = "AvgSensors"
    
    def __init__(self, scenario):
        """
        Initializes the action with the given scenario.
        
        Parameters:
            scenario (Scenario): The scenario containing the sensor history to modify.
        """
        self.topic_history = scenario.topic_history
        self.sensor_name = scenario.sensor_name
        self.topic_list = scenario.topic_list

	def do(self):
		"""
        Computes the average value of the topics and updates the first topic with the result.
        """
		sensor_history = self.topic_history.get_sensor_history(self.sensor_name)
		history_lst = sensor_history.history
		
		if len(history_lst) < 1:
			return

		avg = 0
		last_record = sensor_history.top()
		if type(last_record) is dict:
			for sensor in self.topic_list:
				avg += last_record[sensor]
			avg = avg / len(self.topic_list)
			history_lst[-1][self.topic_list[0]] = avg
		else:
			for sensor in self.topic_list:
				if not hasattr(last_record,sensor):
					raise KeyError("topic " + str(sensor) +" is not defined in "+str(type(last_record)))
				avg += getattr(last_record,sensor)
			avg = avg / len(self.topic_list)
			setattr(history_lst[-1],self.topic_list[0],avg)