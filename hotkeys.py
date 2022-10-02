from loguru import logger
logger.debug("Enter module")

import threading
from pynput import keyboard
import time
import functions as f

def _parse_hotkeys(key_or_char, keyPressed, c):
    logger.debug("Enter. *key_or_char:{} *keyPressed:{}", key_or_char, keyPressed)
    option_temp = "" 
    
    for option in c.obj[c.Hotkeys]: 
        option_temp = c.obj[c.Hotkeys][option] 
        if (key_or_char == "key"): 
            option_temp = 'Key.' + c.obj[c.Hotkeys][option] 
        if (key_or_char == "char"): 
            option_temp = "\'" + str(c.obj[c.Hotkeys][option]) + "\'" 
        
        if(option_temp == keyPressed): 
            return option
            
def _all_hotkeys(hotkey_name, root, rootHidden, guiShown, c): 
    logger.debug("Enter")
    
    
    if(hotkey_name == c.ShowBackground): 
        guiShown.time_1_label.config(bg = c.obj[c.Gui][c.HighlightColor]) 
        guiShown.time_2_label.config(bg = c.obj[c.Gui][c.HighlightColor])
    if(hotkey_name == c.ExitTarkovTime): 
        pass
    
    
    if(hotkey_name == c.MoveToCenter): 
        f.screen_placement(root, c, True)
        pass
    if(hotkey_name == c.ExitTarkovTime): 
        f.destroy(rootHidden)
    if(hotkey_name == c.HideShowTarkovTime): 
        f.toggle_show_hide(root, c)
        

class Hotkeys(): 
    logger.debug("Enter")
    hotkey_name = ""
    def __init__(self, root, rootHidden, guiShown, gui_interact, c):
        logger.debug("Enter. Hotkeys loaded")
        
        def on_press(key):
            logger.debug("Enter {}", key)
            
            try: 
                gui_interact.key_pressed_label.config(text=key)
            except: 
                pass
            temp = key
            keyPressed = str(temp)
            
            key_or_char = ""
            try: 
                test_if_key_or_char = key.char
                key_or_char = "char"
            except: 
                key_or_char = "key" 
            
            if (keyPressed[-1] == '>'):
                key_or_char = "num"
                
            
            self.hotkey_name = _parse_hotkeys(key_or_char, keyPressed, c)
            
            if (self.hotkey_name != None): 
                _all_hotkeys(self.hotkey_name, root, rootHidden, guiShown, c)
        
        def reset_backgroundcolor():
            logger.debug("Enter")
            guiShown.time_1_label.config(bg = c.obj[c.Gui][c.BackgroundColor])
            guiShown.time_2_label.config(bg = c.obj[c.Gui][c.BackgroundColor])
        
        def on_release(key): 
            if(self.hotkey_name == c.ShowBackground):
                #logger.debug("Enter")
                timer = threading.Timer(int(c.obj[c.HotkeyConfig][c.ShowBackgroundDuration]), reset_backgroundcolor)
                timer.start() 

        with keyboard.Listener(
                #suppress=True, # https://pynput.readthedocs.io/en/latest/faq.html
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
        
        # ...or, in a non-blocking fashion:
        """
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        listener.start()
        """