from Automation.automation_brain import Auto_main_brain,clear_file
from GopiRajSTT.listen import listen
import threading
from DATA.dlg_data import online_dlg,offline_dlg
import random
from TTS.ttsB import speak
from Time_Operations.brain import input_manage,input_manage_Alarm
from Features.check_internet_speed import get_internet_speed
from Brain.brain import Main_Brain
from Features.create_file import create_file
from Vision.Vbrain import *
from Vision.MVbrain import *
from WeatherCheck.check_weather import get_weather_by_address

numbers = ["1:","2:","3:","4:","5:","6:","7:","8:","9:"]
spl_numbers = ["11:","12:"]

ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)



def check_inputs():
    output_text = ""
    while True:
        with open("input.txt","r") as file:
            input_text = file.read().lower()
        if input_text != output_text:
            output_text = input_text
            if output_text.startswith("tell me"):
                output_text = output_text.replace(" p.m.","PM")
                output_text = output_text.replace(" a.m.","AM")
                if "11:" in output_text or "12:" in output_text:    
                    input_manage(output_text)
                    clear_file()
                else:   
                    for number in numbers:
                        if number in output_text:
                            output_text = output_text.replace(number,f"0{number}")
                            input_manage(output_text)
                            clear_file()
            elif output_text.startswith("set alarm"):
                output_text = output_text.replace(" p.m.","PM")
                output_text = output_text.replace(" a.m.","AM")
                if "11:" in output_text or "12:" in output_text:    
                    input_manage_Alarm(output_text)
                    clear_file()
                else:   
                    for number in numbers:
                        if number in output_text:
                            output_text = output_text.replace(number,f"0{number}")
                            input_manage_Alarm(output_text)
                            clear_file()
            elif "check internet speed" in output_text:
                speak("checking your internet speed")
                speed = get_internet_speed()
                speak(f"the device is running on {speed}Mb per second")
            elif "jarvis" in output_text:
                response =Main_Brain(output_text)
                speak(response)
            elif output_text.startswith("create"):
                if "file" in output_text:
                    create_file(output_text)
            elif "what is this" in output_text or "what can you see" in output_text:
                        image_path = "captured_image.png"
                        if capture_image_and_save(image_path):
                            encoded_image = encode_image_to_base64(image_path)
                            answer = vision_brain(encoded_image)
                            speak(answer)
            elif "what is in front of mobile camera" in output_text or "what can you see using mobile camera" in output_text:
                        image_path = "captured_image.png"
                        if capture_image_and_save(image_path):
                            encoded_image = encode_image_to_base64(image_path)
                            answer = mobile_vision_brain(encoded_image)
                            speak(answer)
            elif "check weather" in output_text:
                 text = output_text.replace("check weather in")
                 ans = get_weather_by_address(text)
                 speak(ans)
            else:
                Auto_main_brain(output_text)    

def jarvis():
    clear_file()
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=check_inputs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()