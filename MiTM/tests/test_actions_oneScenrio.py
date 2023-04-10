import MiTM.Scenario  as Scenario
import MiTM.AnomalyObjects.Action  as ActionCtrl
from sensor_msgs.msg import NavSatFix 
import time
import copy

class Dummy(object):
    Name = "DummyDuplicateSensor"
    def __init__(self, scenario):
        return

    def do(self):
        return

def test_Actions_Duplicate_And_WhiteNoise_AnyChange():
    #test that the action is triggered when any change is made
    sensor_name = "global_position"
    scenario = Scenario.OneSensorScenario(sensor_name,["latitude","longitude"],steps_back=2)
    scenario.topic_history.add_sensor(sensor_name,None)
    action1 = ActionCtrl.Duplicate(scenario)
    action2 = ActionCtrl.AddWhiteNoise(scenario)

    for i in range(0,10):
        gps_pos = NavSatFix()
        gps_pos.header.frame_id = "world"+str(i)
        gps_pos.header.stamp = time.time()
        gps_pos.status.status = 0 + i
        gps_pos.status.service = 1 + i
        gps_pos.latitude = 34.5 + i
        gps_pos.longitude = 33.2 + i
        gps_pos.altitude = 0.0
        gps_pos.position_covariance = [3.24, 0, 0, 0, 3,24, 0, 0, 0, 0]
        gps_pos.position_covariance_type = 2 + i
        data_before = copy.copy(gps_pos)
        scenario.topic_history.save(sensor_name,gps_pos)

    action1.do()
    data_after = scenario.topic_history.get_sensor_history(sensor_name).top()
    assert data_before != data_after
    
    action2.do()
    data_after = scenario.topic_history.get_sensor_history(sensor_name).top()
    print(data_after)
    assert data_before != data_after



def test_Action_WhiteNoise_AnyChange():
    #test that the action is triggered when any change is made
    sensor_name = "global_position"
    scenario = Scenario.OneSensorScenario(sensor_name,["latitude","longitude"])
    scenario.topic_history.add_sensor(sensor_name,None)
    action = ActionCtrl.AddWhiteNoise(scenario)

    gps_pos = NavSatFix()
    gps_pos.header.frame_id = "world"
    gps_pos.header.stamp = time.time()
    gps_pos.status.status = 0
    gps_pos.status.service = 1
    gps_pos.latitude = 34.5
    gps_pos.longitude = 33.2
    gps_pos.altitude = 0.0
    gps_pos.position_covariance = [3.24, 0, 0, 0, 3,24, 0, 0, 0, 0]
    gps_pos.position_covariance_type = 2
    data_before = copy.copy(gps_pos)
    scenario.topic_history.save(sensor_name,gps_pos)
    action.do()
    data_after = scenario.topic_history.get_sensor_history(sensor_name).top()
    print(data_after)
    assert data_before != data_after

def test_Action_Random_AnyChange():
    #test that the action is triggered when any change is made
    sensor_name = "global_position"
    scenario = Scenario.OneSensorScenario(sensor_name,["latitude","longitude"])
    scenario.topic_history.add_sensor(sensor_name,None)
    action = ActionCtrl.RandomChange(scenario)

    gps_pos = NavSatFix()
    gps_pos.header.frame_id = "world"
    gps_pos.header.stamp = time.time()
    gps_pos.status.status = 0
    gps_pos.status.service = 1
    gps_pos.latitude = 34.5
    gps_pos.longitude = 33.2
    gps_pos.altitude = 0.0
    gps_pos.position_covariance = [3.24, 0, 0, 0, 3,24, 0, 0, 0, 0]
    gps_pos.position_covariance_type = 2
    data_before = copy.copy(gps_pos)
    scenario.topic_history.save(sensor_name,gps_pos)
    action.do()
    data_after = scenario.topic_history.get_sensor_history(sensor_name).top()
    #print(data_after)
    assert data_before != data_after

def test_Action_Duplicate_AnyChange():
    #test that the action is triggered when any change is made
    sensor_name = "global_position"
    scenario = Scenario.OneSensorScenario(sensor_name,["latitude","longitude"],steps_back=2)
    scenario.topic_history.add_sensor(sensor_name,None)
    action = ActionCtrl.Duplicate(scenario)

    for i in range(0,10):
        gps_pos = NavSatFix()
        gps_pos.header.frame_id = "world"+str(i)
        gps_pos.header.stamp = time.time()
        gps_pos.status.status = 0 + i
        gps_pos.status.service = 1 + i
        gps_pos.latitude = 34.5 + i
        gps_pos.longitude = 33.2 + i
        gps_pos.altitude = 0.0
        gps_pos.position_covariance = [3.24, 0, 0, 0, 3,24, 0, 0, 0, 0]
        gps_pos.position_covariance_type = 2 + i
        data_before = copy.copy(gps_pos)
        scenario.topic_history.save(sensor_name,gps_pos)

    action.do()
    data_after = scenario.topic_history.get_sensor_history(sensor_name).top()
    #print(data_after)
    assert data_before != data_after

def test_Action_Disconnect_Default_AnyChange():
    #test that the action is triggered when any change is made
    sensor_name = "global_position"
    scenario = Scenario.OneSensorScenario(sensor_name,["latitude","longitude"])
    scenario.topic_history.add_sensor(sensor_name,None)
    action = ActionCtrl.DisconnectSensor(scenario)

    gps_pos = NavSatFix()
    gps_pos.header.frame_id = "world"
    gps_pos.header.stamp = time.time()
    gps_pos.status.status = 0
    gps_pos.status.service = 1
    gps_pos.latitude = 34.5
    gps_pos.longitude = 33.2
    gps_pos.altitude = 0.0
    gps_pos.position_covariance = [3.24, 0, 0, 0, 3,24, 0, 0, 0, 0]
    gps_pos.position_covariance_type = 2
    data_before = copy.copy(gps_pos)
    scenario.topic_history.save(sensor_name,gps_pos)
    action.do()
    data_after = scenario.topic_history.get_sensor_history(sensor_name).top()
    #print(data_after)
    assert data_before != data_after

def test_Action_Disconnect_1000_AnyChange():
    #test that the action is triggered when any change is made
    sensor_name = "global_position"
    scenario = Scenario.OneSensorScenario(sensor_name,["latitude","longitude"],disconnect_value=1000)
    scenario.topic_history.add_sensor(sensor_name,None)
    action = ActionCtrl.DisconnectSensor(scenario)

    gps_pos = NavSatFix()
    gps_pos.header.frame_id = "world"
    gps_pos.header.stamp = time.time()
    gps_pos.status.status = 0
    gps_pos.status.service = 1
    gps_pos.latitude = 34.5
    gps_pos.longitude = 33.2
    gps_pos.altitude = 0.0
    gps_pos.position_covariance = [3.24, 0, 0, 0, 3,24, 0, 0, 0, 0]
    gps_pos.position_covariance_type = 2
    data_before = copy.copy(gps_pos)
    scenario.topic_history.save(sensor_name,gps_pos)
    action.do()
    data_after = scenario.topic_history.get_sensor_history(sensor_name).top()
    #print(data_after)
    assert data_before != data_after

def test_Action_Avg_AnyChange():
    #test that the action is triggered when any change is made
    sensor_name = "global_position"
    scenario = Scenario.OneSensorScenario(sensor_name,["latitude","longitude"],disconnect_value=1000)
    scenario.topic_history.add_sensor(sensor_name,None)
    action = ActionCtrl.AvgSensors(scenario)

    gps_pos = NavSatFix()
    gps_pos.header.frame_id = "world"
    gps_pos.header.stamp = time.time()
    gps_pos.status.status = 0
    gps_pos.status.service = 1
    gps_pos.latitude = 34.5
    gps_pos.longitude = 33.2
    gps_pos.altitude = 0.0
    gps_pos.position_covariance = [3.24, 0, 0, 0, 3,24, 0, 0, 0, 0]
    gps_pos.position_covariance_type = 2
    data_before = copy.copy(gps_pos)
    scenario.topic_history.save(sensor_name,gps_pos)
    action.do()
    data_after = scenario.topic_history.get_sensor_history(sensor_name).top()
    #print(data_after)
    assert data_before != data_after
