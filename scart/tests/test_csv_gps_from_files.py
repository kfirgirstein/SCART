#test history and anomalies 
import scart.Scenario  as Scenario
import scart.AnomalyObjects.Action  as ActionCtrl
import scart.AnomalyObjects.Condition  as ConditionCtrl
import scart.AnomalyObjects.Listener  as ListenerCtrl
import json
import numpy as np
import pandas as pd
from random import SystemRandom
np.random.seed( SystemRandom().randrange(0,2**32 -1))

PARAMETERS_FILE = "/home/makery/Desktop/tools/AADRT/csv_parameter_example.json"
STRING_TO_ACTION = {
    "Duplicate": ActionCtrl.Duplicate,
    "AvgSensors": ActionCtrl.AvgSensors,
    "DisconnectSensor": ActionCtrl.DisconnectSensor,
    "RandomChange": ActionCtrl.RandomChange,
    "AddWhiteNoise"
    : ActionCtrl.AddWhiteNoise,
}
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
        self.current_scenario.starting_conditions = ConditionCtrl.GetIteration(self.current_scenario)
        self.current_scenario.ending_conditions = ConditionCtrl.EndTime(self.current_scenario)
        self.current_scenario.actions = STRING_TO_ACTION[self._action.strip()](self.current_scenario)
        self.current_scenario.listeners = ListenerCtrl.SimpleListener(self.current_scenario)
        self.current_scenario.install_scenario()
        
    def test_gps_dup(self):
        df = pd.read_csv(self.env_parameters["file_path"] + self.env_parameters["file_name"])
        topic_new_data = df[self.topic_list]

        for index,row in topic_new_data.iterrows():
            self.current_scenario.listener(row)
            for topic in self.topic_list:
                df.at[index,topic] = row[topic]
        
        return df



def main(argv):

    if len(argv) < 2 :
        print("Usage: python test_csv_gps_from_files.py <parameters_file>")
        return 1

    PARAMETERS_FILE = argv[1]

    with open(PARAMETERS_FILE) as f:
        parameters = json.load(f)

    scenario = GPSDuplicateScenario(**parameters)
    scenario.init_scenario()
    new_df = scenario.test_gps_dup()
    
    if "to_file_name" in parameters["env_parameters"] and parameters["env_parameters"]["to_file_name"] != None:
        new_df.to_csv(parameters["env_parameters"]["to_file_name"])

        
    if "debug" in parameters["env_parameters"]:
        scenario.print_sensor_changes()
    

    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    print("finish")

    








