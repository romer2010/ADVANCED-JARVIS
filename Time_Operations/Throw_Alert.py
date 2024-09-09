import os
import time
import threading
from Alert import Alert
from TTS.ttsB import speak
import threading
from os import getcwd



def load_schedule(file_path):
    schedule = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    line_time, activity = line.strip().split(' = ')
                    schedule[line_time.strip()] = activity.strip()
    except Exception as e:
        print(f"Error loading schedule: {e}")
    return schedule

def check_schedule(file_path):
    last_modified = 0
    while True:
        current_time = time.strftime("%I:%M%p")
        try:
            # Check file modification time
            modified = os.path.getmtime(file_path)
            if modified != last_modified:
                last_modified = modified
                schedule = load_schedule(file_path)
            
            if current_time in schedule:
                text = schedule[current_time]
                t1 = threading.Thread(target=Alert, args=(text,))
                t2 = threading.Thread(target=speak, args=(text,))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
        
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(60)

def load_AlarmTime(file_path):
    schedule = {}
    try:
        with open(file_path, 'r') as file:
            schedule = file.read()
    except Exception as e:
        print(f"Error loading schedule: {e}")
    return schedule

alarm_path = r"C:\Users\GOPI RAJ\Desktop\ADVANCED JARVIS\Alarm_data.txt"

def check_Alarm(alarm_path):
    last_modified = 0
    while True:
        current_time = time.strftime("%I:%M%p")
        try:
            # Check file modification time
            modified = os.path.getmtime(alarm_path)
            if modified != last_modified:
                last_modified = modified
                schedule = load_AlarmTime(alarm_path)
            
            if current_time in schedule:
                text = "This is Alarm"
                t1 = threading.Thread(target=Alert, args=(text,))
                t2 = threading.Thread(target=speak, args=(text,))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
        
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(10)
