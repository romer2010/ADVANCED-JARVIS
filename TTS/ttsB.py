import requests
from playsound import playsound
import os
from typing import Union
import sys
import time
import threading

def generate_audio(message: str,voice : str = "Brian"):
    url: str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={{{message}}}"

    headers = {'user-agent':'Mozilla/5.0(Maciontosh;intel Mac os x 10_15_7)AppleWebKit/537.36(KHTML,like Gecoko)Chrome/119.0.0.0 Safari/537.36'}
    
    try:
        result = requests.get(url=url, headers=headers)
        return result.content
    except:
        return None
    
def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.050)  # Adjust the sleep duration for the animation speed
    print()

def Co_speak(message: str, voice: str = "Brian", folder: str = "", extension: str = ".mp3") -> Union[None, str]:
    try:
        result_content = generate_audio(message,voice)
        file_path = os.path.join(folder,f"{voice}{extension}")
        with open(file_path, "wb") as file:
            file.write(result_content)
        playsound(file_path)
        os.remove(file_path)
        return None
    except Exception as e:
        print(e)

def speak(text):
    t1 = threading.Thread(target=Co_speak,args=(text,))
    t2 = threading.Thread(target=print_animated_message,args=(text,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()