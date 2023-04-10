from random import SystemRandom
from .AbstractActionFile import AbstractAction
import numpy as np

is_DEBUG = True
class RandomChange(AbstractAction):
	Name = "Random_lat_lon"
	
	def __init__(self, scenario):
		self.topic_history = scenario.topic_history
		self.sensor_name = scenario.sensor_name
		self.topic_list = scenario.topic_list
		np.random.seed( SystemRandom().randrange(0,2**32 -1))
		
		
	def do(self):
		sensor_history = self.topic_history.get_sensor_history(self.sensor_name)
		history_lst = sensor_history.history

		#randomly select a topic to change
		if len(history_lst) < 1:
			return

		last_record = sensor_history.top()
		if type(last_record) is dict:
			for sensor in self.topic_list:
				last_sensor_record = last_record[sensor]
				history_lst[-1][sensor] = np.random.normal(last_sensor_record,last_sensor_record,1)
		else:
			for sensor in self.topic_list:
				if not hasattr(last_record,sensor):
					raise KeyError("topic " + str(sensor) +" is not defined in "+str(type(last_record)))

				last_sensor_record = getattr(last_record,sensor)
				setattr(last_record,sensor,np.random.normal(last_sensor_record,last_sensor_record,1))