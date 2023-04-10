from .AbstractActionFile import AbstractAction

class Duplicate(AbstractAction):
	Name = "DuplicateSensor"
	
	def __init__(self, scenario):
		self.topic_history = scenario.topic_history
		self.sensor_name = scenario.sensor_name
		self.topic_list = scenario.topic_list

		#if steps_back not defined
		if (not hasattr(scenario,"steps_back")):
			scenario.steps_back = 0
			
		#if steps_back is negative
		if scenario.steps_back > 0 :
			scenario.steps_back = -scenario.steps_back

		self.steps_back = scenario.steps_back
		
		
	def do(self):
		sensor_history = self.topic_history.get_sensor_history(self.sensor_name)
		history_lst = sensor_history.history
		
		last_record = sensor_history.top()
		if type(last_record) is dict:
			for sensor in self.topic_list:
				history_lst[-1][sensor] = history_lst[0][sensor]
		else:
			for sensor in self.topic_list:
				if not hasattr(last_record,sensor):
					raise KeyError("topic " + str(sensor) +" is not defined in "+str(type(last_record)))
				setattr(history_lst[-1],sensor,getattr(history_lst[self.steps_back],sensor))  
