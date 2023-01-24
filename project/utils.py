import json,pickle
import numpy as np
import config

class OxygenFlow():
    def __init__(self,age,gender,spo2,pr,cnc):
        self.age = age
        self.gender = gender
        self.spo2 = spo2
        self.pr = pr
        self.cnc = cnc
    def get_models(self):
        with open(config.json_path, "r") as f:
            self.json_file = json.load(f)
        with open(config.model_path, "rb") as f:
            self.model = pickle.load(f)
        with open(config.scl_path, "rb") as f:
            self.sdt_scl = pickle.load(f)
    def get_oxygen_need(self):
        self.get_models()
        dict1 = {"gender":{"male":1,"female":0},"c/nc":{"positive":1, "negative":0}}
        test_arr = np.zeros(len(self.json_file["columns"]))
        test_arr[0] = self.age
        test_arr[1] = dict1["gender"][self.gender]
        test_arr[2] = self.spo2
        test_arr[3] = self.pr
        test_arr[4] = dict1["c/nc"][self.cnc]

        array = self.sdt_scl.transform([test_arr])
        prediction = self.model.predict(array)
        return prediction
