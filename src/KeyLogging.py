import keyboard

def on_press(event):
    print(event.name)

def on_release(event):
    print("Released")
    print('Key', event.name, 'released')

# set up event listeners
keyboard.on_press(on_press)
keyboard.on_release(on_release)

# start the event loop
keyboard.wait()