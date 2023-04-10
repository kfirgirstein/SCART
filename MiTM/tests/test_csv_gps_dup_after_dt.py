#test history and anomalies 
import MiTM.Scenario  as Scenario
import MiTM.AnomalyObjects.Action  as ActionCtrl
import MiTM.AnomalyObjects.Condition  as ConditionCtrl
import MiTM.AnomalyObjects.Listener  as ListenerCtrl
import json
import numpy as np
import pandas as pd
from random import SystemRandom
np.random.seed( SystemRandom().randrange(0,2**32 -1))

PARAMETERS_FILE = "/home/makery/Desktop/tools/AADRT/csv_parameter_example.json"

class GPSDuplicateScenario():
    def __init__(self,**kwargs):
        self.current_scenario = None
        self.__dict__.update(kwargs)

    def print_sensor_changes(self):
        df = pd.read_csv(self.env_parameters["file_path"] + self.env_parameters["file_name"])
        gps_history = df[self.topic_list]
        topic_new_data = self.current_scenario.topic_history.get_sensor_history(self.sensor_name).history
        for index,row in gps_history.iterrows():
            if index > self.extra_parameters["starting_time"]:
                print("Before:\n" + str(row[self.topic_list]) + "\nAfter:\n" + str(topic_new_data[index]))
            if index > self.extra_parameters["starting_time"] + self.extra_parameters["duration"] + 5 :
                break
        
    def parameters_to_string(self):
        msg = "parameters for this run:\n{\n"
        for key,value in self.current_scenario.__dict__.items():
            msg += "\t" + key + " => " + str(value) + "\n"
        msg += "}"
        return msg

    def init_scenario(self):
        self.current_scenario = Scenario.OneSensorScenario(self.sensor_name,self.topic_list,**self.extra_parameters)
        self.current_scenario.starting_conditions = ConditionCtrl.GetTimestamp(self.current_scenario)
        self.current_scenario.end_conditions = ConditionCtrl.EndTime(self.current_scenario)
        action_list = [ActionCtrl.Duplicate(self.current_scenario),\
                        ActionCtrl.AvgSensors(self.current_scenario),\
                            ActionCtrl.DisconnectSensor(self.current_scenario),\
                                ActionCtrl.RandomChange(self.current_scenario),\
                                    ActionCtrl.AddWhiteNoise(self.current_scenario)]
        self.current_scenario.actions = np.random.choice(action_list)
        self.current_scenario.listeners = ListenerCtrl.SimpleListener(self.current_scenario)
        self.current_scenario.install_scenario()
        
    def test_gps_dup(self):
        df = pd.read_csv(self.env_parameters["file_path"] + self.env_parameters["file_name"])
        topic_new_data = df[self.topic_list]

        #TODO: save df to new csv file
        for index,row in topic_new_data.iterrows():
            self.current_scenario.listener(row)
        


def main():
    with open(PARAMETERS_FILE) as f:
        parameters = json.load(f)

    scenario = GPSDuplicateScenario(**parameters)
    scenario.init_scenario()
    scenario.test_gps_dup()
    
    #TODO: check if debug is on, and then print the changes
    #TODO: check if save is on, and then save the changes
    scenario.print_sensor_changes()
        
    
if __name__ == '__main__':
    main()
    print("finish")

    








