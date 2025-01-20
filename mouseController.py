from pynput.mouse import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (500,500) # X Axis, Y Axis

controlMouse()

