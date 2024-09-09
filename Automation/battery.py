import psutil
import time
from TTS.ttsB import speak
import threading
from Alert import Alert


battery = psutil.sensors_battery()

def battery_Alert():
    while True:
        time.sleep(3)
        percentage = int(battery.percent)
        if percentage == 100:
            t1 = threading.Thread(target=Alert,args=("100% charge",))
            t2 = threading.Thread(target=speak,args=("100% charged please unplug it",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <=20:
            t1 = threading.Thread(target=Alert,args=("Battery Low",))
            t2 = threading.Thread(target=speak,args=("SIR, SORRY TO DISTURB YOU ! YOUR BATTERY IS LOW NOW",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <=10:
            t1 = threading.Thread(target=Alert,args=("Battery Critical",))
            t2 = threading.Thread(target=speak,args=("SIR, SORRY TO DISTURB YOU! YOUR BATTERY IS CRITICAL NOW",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()    
        elif percentage <=5:
            t1 = threading.Thread(target=Alert,args=("Battery About to Die",))
            t2 = threading.Thread(target=speak,args=(" YOUR BATTERY IS ABOUT TO DIE",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        time.sleep(10)

def check_plug():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged
    while True:
        battery = psutil.sensors_battery()
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                t1 = threading.Thread(target=Alert,args=("CHARGING...",))
                t2 = threading.Thread(target=speak,args=("PLUGGED IN",))
                t1.start()
                t2.start()
                t1.join()
                t2.join()               
            else:
                t1 = threading.Thread(target=Alert,args=("CHARGING STOPPED",))
                t2 = threading.Thread(target=speak,args=("PLUGGED OUT",))
                t1.start()
                t2.start()
                t1.join()
                t2.join()

            previous_state = battery.power_plugged

def check_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    t1 = threading.Thread(target=Alert,args=(f"The Device Is Running On {percent}% Power",))
    t2 = threading.Thread(target=speak,args=(f"The Device Is Running On {percent}% Power",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

