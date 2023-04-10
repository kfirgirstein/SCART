class BasicScenarioCallback():
    def __init__(self,starting_cond,ending_cond,action_ctrl):
        self.__starting_cond = starting_cond
        self.__ending_cond = ending_cond
        self.__action_ctrl = action_ctrl
    
    def GetScenarioCallback(self):
        return lambda: self.scenario_callback()
        
    def scenario_callback(self):
        try:
            if self.__starting_cond.check_condition() and not self.__ending_cond.check_condition():
                self.__action_ctrl.do()

        except Exception as e:
            print(e)
            print("error in scenario callback")
            return False
        return True

class A():
    def check_condition(self):
        print("a")
        return True

class B():
    def check_condition(self):
        print("b")
        return False

class C():
    def do(self):
        print("c")
        
if __name__ == "__main__":
    s = BasicScenarioCallback(A(),B(),C())
    callback = s.GetScenarioCallback()
    callback()

