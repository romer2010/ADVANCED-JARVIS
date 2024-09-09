from Automation.open_app import open_App
from Automation.web_open import openweb
import pyautogui as gui
from Automation.play_music_yt import play_music_on_youtube
from TTS import ttsB
from Automation.play_spotify import play_music_on_spotify
from Automation.battery import check_percentage
from os import getcwd
import time
from Automation.tab_automation import perform_action
from Automation.yt_play_back import perform_media_action
import pywhatkit
from Automation.scroll_system import perform_scroll_action
import threading
from TTS.ttsB import speak

def play():
    gui.press("space")


def search_google(text):
    pywhatkit.search(text)




def close():
    gui.hotkey('alt','f4')


def search(text):
    gui.press("/")
    time.sleep(0.3)
    gui.write(text)
        

def Open_Brain(text):
    if "website" in text or "open website name" in text or ".com" in text:
        text = text.replace("open","").strip()
        text = text.replace("website","").strip()
        text = text.replace("open website name","").strip()
        text = text.replace(".com","").strip()
        t1 = threading.Thread(target=speak,args=(f"Navigating {text} website",))
        t2 = threading.Thread(target=openweb,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        text = text.replace("open","").strip()
        text = text.replace("app","").strip()
        t1 = threading.Thread(target=speak,args=(f"Navigating {text} application",))
        t2 = threading.Thread(target=open_App,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

def clear_file():
    with open(f"{getcwd()}\\input.txt","w") as file:
        file.truncate(0)

def Auto_main_brain(text):
    try:
        if text.startswith("open"):
            Open_Brain(text)
        elif "close" in text:
            close()
        elif "kaisa hai bhai tu" in text or "kaisa hai bhai" in text:
            ttsB.speak("I am good sir , what about you ?")
            clear_file()
        elif "mai bhi acha hoon" in text or "i am good too" in text or "mai bhi acha hun" in text or "i am good to" in text:
            ttsB.speak("Nice to hear that , sir")
            clear_file()
        elif "aur btao" in text or "aur batao" in text:
            ttsB.speak("HOW CAN I HELP YOU  , SIR ?")
            clear_file()
        elif "tell me about yourself" in text or "Apne bare mein batao" in text or "about you" in text or "apne bare mein batao" in text:
            ttsB.speak("I am an AI , developed by Gopi Raj, and my purpose is to help you with your daily tasks. I can answer questions, play music, browse the internet, and perform other useful tasks.")
            clear_file()
        elif "play music" in text or "play music on youtube" in text: 
            ttsB.speak("which song do you want to play sir.") 
            clear_file()
            output_text = ""
            while True:
                with open("input.txt","r") as file:
                    input_text = file.read().lower()
                if input_text != output_text:
                    output_text = input_text
                    if output_text.endswith("song"):
                        play_music_on_youtube(output_text)
                        break
            else:
                pass    

        elif "play music on spotify" in text or "play some music" in text:
            ttsB.speak("which song do you want to play sir.")
            clear_file()
            output_text = ""
            while True:
                with open("input.txt","r") as file:
                    input_text = file.read().lower()
                if input_text != output_text:
                    output_text = input_text
                    if output_text.endswith("song"):
                        play_music_on_spotify(output_text)
                        break
        elif "check battery percentage" in text or "check battery level" in text:
            check_percentage()
        elif text.startswith("search"):
            text = text.replace("search","")
            text = text.strip()
            t1 = threading.Thread(target=speak,args=(f"Doing research about {text}",))
            t2 = threading.Thread(target=search,args=(text,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            time.sleep(0.5)
            gui.press("enter")
        elif "search in google" in text:
            text = text.replace("search in google","")
            t1 = threading.Thread(target=speak,args=(f"performing research about {text} in google search engine",))
            t2 = threading.Thread(target=search_google,args=(text,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif "play" in text or "pause" in text or "stop" in text:
            play()         
        else:
            perform_action(text)
            perform_media_action(text)
            perform_scroll_action(text)
    except Exception as e:
        print(f"An error occurred: {e}")
 
