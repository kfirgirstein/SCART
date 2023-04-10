#test history and anomalies 
import MiTM.Scenario  as Scenario
import MiTM.AnomalyObjects.Action  as ActionCtrl
import MiTM.AnomalyObjects.Condition  as ConditionCtrl
import MiTM.AnomalyObjects.Listener  as ListenerCtrl
import json
import rospy
from std_msgs.msg import String #rosbag info x.bag
from sensor_msgs.msg import NavSatFix #http://docs.ros.org/en/api/sensor_msgs/html/msg/NavSatFix.html
import numpy as np
from random import SystemRandom
np.random.seed( SystemRandom().randrange(0,2**32 -1))

PARAMETERS_FILE = "sim_paramerts_example.json"

class ROSGPSDuplicateScenario():
    def __init__(self,**kwargs):
        self.current_scenario = None
        self.pub = None
        self.__dict__.update(kwargs)

    def init_scenario(self):
        self.current_scenario = Scenario.OneSensorScenario(self.sensor_name,self.topic_list,**self.extra_parameters)
        self.current_scenario.starting_conditions = ConditionCtrl.GetTimestamp(self.current_scenario)
        self.current_scenario.ending_conditions = ConditionCtrl.EndTime(self.current_scenario)
        action_list = [ActionCtrl.Duplicate(self.current_scenario),\
                        ActionCtrl.AvgSensors(self.current_scenario),\
                            ActionCtrl.DisconnectSensor(self.current_scenario),\
                                ActionCtrl.RandomChange(self.current_scenario),\
                                    ActionCtrl.AddWhiteNoise(self.current_scenario)]
        self.current_scenario.actions = np.random.choice(action_list)
        self.current_scenario.listeners = ListenerCtrl.SimpleListener(self.current_scenario)
        self.current_scenario.install_scenario()

    def parameters_to_string(self):
        msg = "parameters for this run:\n{\n"
        for key,value in self.current_scenario.__dict__.items():
            msg += "\t" + key + " => " + str(value) + "\n"
        msg += "}"
        return msg

    def gps_subscriber_callback(self,data):
        self.current_scenario.listener(data)
        topic_history = self.current_scenario.topic_history
        self.pub.publish(topic_history.get_sensor_history(self.sensor_name).top())

    def ros_listener(self):
        print(self.parameters_to_string())
        return 
        rospy.init_node('gps_handle_node', anonymous=True)
        rospy.loginfo("Started gps mitm node")

        self.pub = rospy.Publisher(self.from_topic, NavSatFix, queue_size=10)
        rospy.Subscriber(self.to_topic, NavSatFix, lambda data: self.gps_subscriber_callback(data))

        rospy.spin()

def change_randomly_params(params):

    #for key,value in params.items():
     #   value = np.abs(int(np.random.normal(value,value,1)))
      #  params[key] = value

    if "starting_time" in params:
        params["starting_time"] = np.random.randint(400,1200)

    if "sigma" in params:
        params["sigma"] = np.random.normal(params["sigma"],params["sigma"],1)[0]

    if "steps_back" in params:
        params["steps_back"] = np.abs(int(np.random.normal(params["steps_back"],params["steps_back"],1)))

    return params

def main():
    with open(PARAMETERS_FILE) as f:
        parameters = json.load(f)

    parameters["extra_parameters"] = change_randomly_params(parameters["extra_parameters"])
    #print(json.dumps(parameters, indent=4))
    scenario = ROSGPSDuplicateScenario(**parameters)
    scenario.init_scenario()
    scenario.ros_listener()
    

if __name__ == '__main__':
    main()
    








