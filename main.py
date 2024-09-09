from TTS import ttsB
from GopiRajSTT.listen import listen
import threading


def check():
    output_text = ""
    while True:
        try:
            with open("input.txt", 'r') as file:
                input_text = file.read().lower().strip()
                if input_text != output_text:
                    output_text = input_text
                    if output_text:
                        ttsB.speak(output_text)
        except FileNotFoundError:
            pass

t1 = threading.Thread(target=listen)
t2 = threading.Thread(target=check)
t1.start()
t2.start()
t1.join()
t2.join()                    
