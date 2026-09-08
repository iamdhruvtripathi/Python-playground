from pynput import keyboard
from playsound3 import playsound

def fart():
    playsound("fart-with-reverb.mp3")

def on_press(key):
    try:
        if key.char == "f":
            fart()
    except AttributeError:
        if key == keyboard.Key.esc:
            return False

print("Fart machine armed")
print("Press F to fart. Press ESC to quit.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
