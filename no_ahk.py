    from pynput import keyboard


    #if not using ahk
    def on_press(key):
        try:
            if key == keyboard.KeyCode(char='F9'):
                print('Key a pressed')
        except AttributeError:
            print('special key pressed {0}'.format(key))

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()    
