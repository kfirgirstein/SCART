#test hisotry and anomlies 

import MiTM.history as history
import pandas as pd
from threading import Timer
import numpy as np

FILE_PATH = "~/Desktop/regualr_log/2021-12-01"
FILE_NAME = "/merge/26/filtered.csv"
TOPIC_LIST = ["lat","lon"]
SENSOR_NAME = "GPS"
STATING_TIME = 15800
DURATION = 5000

def starting_condition():
    global topic_history
    gps_history = topic_history.get_sensor_history(SENSOR_NAME)
    if len(gps_history) > STATING_TIME and not ending_condition():
        anomlies()

def ending_condition():
    global DURATION
    if DURATION >= 0:
        DURATION -=  1
        return False
    return True 

def anomlies():
    global topic_history
    gps_history = topic_history.get_sensor_history(SENSOR_NAME)
    history_lst = gps_history.history
    history_lst[-1] = history_lst[-STATING_TIME]

def listener(elem):
    global topic_history
    topic_history.save(SENSOR_NAME,elem)


df = pd.read_csv(FILE_PATH+FILE_NAME)

topic_new_data = df[TOPIC_LIST]
topic_history = history.HistoryHolder()
topic_history.add_sensor(SENSOR_NAME,starting_condition)
for index,row in topic_new_data.iterrows():
    listener(row)
    #t = Timer(0.01 , listener,[row])
    #t.start() 

gps_history = topic_history.get_sensor_history(SENSOR_NAME).history
for index,row in topic_new_data.iterrows():
    if index > STATING_TIME:
        print("before:",row["lat"],row["lon"],"\nafter:",gps_history[index]["lat"],gps_history[index]["lon"])
    if index > STATING_TIME + 5000 + 5 :
        break
    








