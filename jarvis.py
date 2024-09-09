import threading
from internet_check import is_Online
from Alert import Alert
from DATA.dlg_data import online_dlg,offline_dlg
import random
from co_brain import jarvis
from TTS.ttsB import speak
from Automation.battery import check_plug
from Time_Operations.Throw_Alert import check_schedule,check_Alarm

alarm_path = r"C:\Users\GOPI RAJ\Desktop\ADVANCED JARVIS\Alarm_data.txt"
file_path = r'C:\Users\GOPI RAJ\Desktop\ADVANCED JARVIS\schedule.txt'

ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)

def wish():
        t1 = threading.Thread(target=speak,args=(ran_online_dlg,))
        t2 = threading.Thread(target=Alert,args=(ran_online_dlg,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

def main():
    if is_Online():
        wish()
        t3 = threading.Thread(target=check_plug)
        t4 = threading.Thread(target=check_schedule,args=(file_path,))
        t5 = threading.Thread(target=jarvis)
        t6 = threading.Thread(target=check_Alarm,args=(alarm_path,))
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
    else:
        Alert(ran_offline_dlg)
main()