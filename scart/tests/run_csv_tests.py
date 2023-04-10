import test_csv_gps_from_files
import numpy as np
from random import SystemRandom
np.random.seed( SystemRandom().randrange(0,2**32 -1))
import os
import json

PARMS_DIR = "/home/makery/Desktop/anomly_log/2022-11-08/merge/"
PARMS_JSON_NAME = "csv_parameter_example.json"

RANDOM_FILE_TO_CHOSE = "/home/makery/Desktop/regualr_log/2022-08-22/scart_no_attack_22_08_22/"
OUT_FILE_PATH = "/home/makery/Desktop/anomly_log/2022-11-28/"
FILE_NAMES = ["filtered"]

def get_all_dirs(path):
    dirs = []
    path = path if path[-1] == "/" else path + "/"
    directory_contents = os.listdir(path)
    for item in directory_contents:
        if os.path.isdir(path + item) and "." not in item:
            dirs.append(item)
    return dirs


def mkdir_p(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("---------------{} created! ---------- ".format(path))
    

def update_parameters(param_file):
    with open(param_file) as f:
        parameters = json.load(f)

    choose_id = np.random.choice(get_all_dirs(RANDOM_FILE_TO_CHOSE+"merge/"))
    parameters["env_parameters"]["file_path"] = RANDOM_FILE_TO_CHOSE
    new_params = []
    last_index = len(get_all_dirs(OUT_FILE_PATH)) + 1 
    for file_name in FILE_NAMES:
        parameters["env_parameters"]["file_name"] = "/merge/"+choose_id +"/" + file_name + ".csv"
        mkdir_p("{}/{}".format(OUT_FILE_PATH,last_index))
        parameters["env_parameters"]["to_file_name"] = "{}/{}/{}".format(OUT_FILE_PATH,last_index,file_name + ".csv")
        
        if "starting_time" in parameters["extra_parameters"]:
            parameters["extra_parameters"]["starting_iteration"] = parameters["extra_parameters"]["starting_time"] 
            del parameters["extra_parameters"]["starting_time"] 
        
        if "File" in parameters["_action"]:
            parameters["_action"] = parameters["_action"].replace("File", "").strip()

        new_params.append("{}/{}/{}_csv_parameters.json".format(OUT_FILE_PATH,last_index,file_name))
        with open(new_params[-1], 'w') as f:
            json.dump(parameters, f)

    return new_params

def main():
       
    parms_dir = get_all_dirs(PARMS_DIR)
    for item in parms_dir:
        parms_file = "{}/{}/{}".format(PARMS_DIR,item,PARMS_JSON_NAME)     
        new_parameters_files = update_parameters(parms_file)
        for p_file in new_parameters_files:
            test_csv_gps_from_files.main(["test_csv_gps_from_files.py",p_file])

main()