import webbrowser
import pyautogui as ui
import time

def play_music_on_spotify(song_name):
    webbrowser.open("https://open.spotify.com/")
    time.sleep(7)
    ui.hotkey("ctrl","shift","l")
    time.sleep(2)
    ui.write(song_name)
    time.sleep(1.5)
    ui.leftClick(895,590)
