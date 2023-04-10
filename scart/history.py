
class History(object):
    def __init__(self,name,on_change):
        self.__observer__ = on_change
        self.__name__ =  name
        self.__history__ = []


    def __len__(self):
        return len(self.__history__)

    @property
    def history(self):
       return self.__history__
       
    @history.setter
    def history(self,new):
        self.__history__.append(new)
        if self.observer:
            if type(self.observer) is list:
                for f in self.observer:
                    success = f()
                    if not success:
                        break
            else:
                self.observer()

    @property
    def name(self):
       return self.__name__


    @property
    def observer(self):
        return self.__observer__

    def tail(self):
        return self.__history__[0] if  self.__history__ and len( self.__history__) > 0 else None

    def top(self):
        return self.__history__[-1] if  self.__history__ and len( self.__history__) > 0 else None


    @observer.setter
    def observer(self,on_change):
        if type(on_change) is list:
            self.__observer__.append(on_change)
        else:
            self.__observer__ = on_change



class HistoryHolder(object):
    def __init__(self):
        self._sensors = {}

    def add_sensor(self,sensor_name,on_change):
        if sensor_name in self._sensors:
            if type(self._sensors[sensor_name]) is not History:
                raise Exception("Sensor type initialized without history")
            self._sensors[sensor_name].observer = on_change
        else:
            self._sensors[sensor_name] = History(sensor_name,on_change)

    def save(self,sensor_name,data):
        if not sensor_name in self._sensors:
            raise Exception("Sensor name " +sensor_name+" is not in History")

        self._sensors[sensor_name].history = data

    def get_sensor_history(self,sensor_name):
        if not sensor_name in self._sensors:
            raise Exception("Sensor name " +sensor_name+" is not in History")

        return self._sensors[sensor_name]


            