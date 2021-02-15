from vidstream import ScreenShareClient
import threading
import tkinter as tk
import pyautogui
import time
import keyboard

sender = ScreenShareClient('127.0.0.1', 9999)

t = threading.Thread(target=sender.start_stream)
t.start()


if keyboard.is_pressed("enter"):
    pyautogui.alert("ok")
else:
    pyautogui.alert("Compartilhando tela!")
exit()


while input("") != 'STOP':
    continue

sender.stop_server()
