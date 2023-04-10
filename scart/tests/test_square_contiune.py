from scart import history
import pandas as pd
from threading import Timer
import numpy as np

FILE_PATH = "~/Desktop/regualr_log/2021-12-01"
FILE_NAME = "/merge/26/filtered.csv"
TOPIC = "lat"

def starting_condition():
    global topic_history
    lat_history = topic_history.get_sensor_history("x")
    diff = np.abs(lat_history.top() - lat_history.tail())
    if not pd.isna(diff) and diff >9.9:
        pass
        #print(diff)

def ending_condition():
    pass

def anomalies():
    pass

def listener_converter():
    global topic_history
    lat_history = topic_history.get_sensor_history(TOPIC)
    history_lst = lat_history.history
    if len(history_lst) < 2:
        topic_history.save("x",0)
        return

    diff = history_lst[-1] - history_lst[-2]
    topic_history.save("x",(topic_history.get_sensor_history("x").top() + diff*1e7))


def listener(elem):
    global topic_history
    
    if not elem or pd.isna(elem):
        return

    topic_history.save(TOPIC,elem)

df = pd.read_csv(FILE_PATH+FILE_NAME)
topic_new_data = df[TOPIC]
topic_history = history.HistoryHolder()
topic_history.add_sensor(TOPIC,listener_converter)
topic_history.add_sensor("x",starting_condition)

for d in topic_new_data:
    listener(d)
    #t = Timer(0.01 , listener,[d])
    #t.start() 

xs = topic_history.get_sensor_history("x").history
for i,x in enumerate(xs):
    if x >0:
        print(i,x)
    





