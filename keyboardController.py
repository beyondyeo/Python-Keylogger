from pynput.keyboard import Controller

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Hello World!")

controlKeyboard()

