import imp
import random as rnd
import threading
from .AbstractConditionFile import AbstractCondition

PERIOD_LIMITS1 = 1
PERIOD_LIMITS2 = 10
Frequency = 10

class RandomStart(AbstractCondition):
    def __init__(self, FILE):
        self.FILE = FILE
        self.notonAction = True #if we are in anomaly the value is False else True 
    def check_condition(self):
        topic_history = self.FILE.topic_history
        SENSOR_NAME = self.FILE.SENSOR_NAME
        LOGINFO = self.FILE.LOGINFO
        STATING_TIME = self.FILE.STATING_TIME
        gps_history = topic_history.get_sensor_history(SENSOR_NAME)
        if LOGINFO:
            LOGINFO
        if self.notonAction:
            rnd1 = rnd.randrange(0,Frequency)
            if rnd1 == 1:
                self.notonAction = False
                self.FILE.DURATION = 10
        else:
            anomalies_thread = threading.Thread(target=self.FILE.action.do)
            anomalies_thread.start()
            anomalies_thread.join()
            if self.FILE.DURATION <= 0:
                self.FILE.DURATION = 10
                self.notonAction = True


        self.FILE.topic_history = topic_history 
        self.FILE.SENSOR_NAME = SENSOR_NAME 
        self.FILE.LOGINFO = LOGINFO
        self.FILE.STATING_TIME = STATING_TIME