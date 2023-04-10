from .AbstractActionFile import AbstractAction

# Update the first topic in topic list to the average of the topic list values
class AvgSensors(AbstractAction):
	Name = "AvgSensors"
	def __init__(self,scenario):
		self.topic_history = scenario.topic_history
		self.sensor_name = scenario.sensor_name
		self.topic_list = scenario.topic_list


	def do(self):
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