from .AbstractListenerFile import AbstractListener


class SimpleListener(AbstractListener):
	Name = "SimpleListener"

	def __init__(self,scenario):
		import sys
		if sys.version_info.major == 3:
			super().__init__(scenario)
		else:
			super(SimpleListener,self).__init__(scenario)
		

	def listen(self, element):
		self.topic_history.save(self.sensor_name,element)

	
