from threading import *
# import subprocess
import time

#debug

class LauncherThread(Thread):
    def __init__(self,id,name):
        Thread.__init__(self)
        self.name = name
        self.id = id
    def run(self):
        print("launched",self.id,self.name.split("-"))
        start_time = time.time()  # 记录程序启动时间
        mainpicker()
        end_time = time.time()  # 记录程序结束时间
        elapsed_time = end_time - start_time
        print("completed in", elapsed_time, "s")

def mainpicker():
    open("RandomPicker.exe")


instance1 = LauncherThread(1,"inst1")

instance1.start()