
from loguru import logger
logger.debug("Enter Main module")

import sys
logger.info("User Current Version: {}", sys.version)


import tkinter as tk
import time
import datetime as dt
import os

import threading

from ctypes import windll # windll.shcore.SetProcessDpiAwareness(1)
windll.shcore.SetProcessDpiAwareness(1)

import currenttime
import readwriteconfig
#import hotkeys
import functions as f

import config
c = config.TestClass


def _get_config(obj):
    logger.debug("Enter")
    return readwriteconfig.read_config_file(obj) #.writeDefaultConfig()


class main():
    logger.debug("Enter")
    def __init__(self):
        logger.debug("Enter")
        #c.obj = readwriteconfig.read_config_file(c.obj)
        c.obj = _get_config(c.obj)
        
        
        rootHidden = RootHidden() #tk.Tk()
        guiHidden = GuiThings(rootHidden)
        root = RootShown(rootHidden)
        guiShown = GuiThings(root)
        try:
            rootHidden.iconbitmap('./icon.ico')
            rootHidden.iconbitmap('./config/icon.ico')
        except: 
            pass
        
        irl_start_time = f.to_time_format(c.obj[c.TimeSettings][c.TimeStartIRL])
        eft_start_time = f.to_time_format(c.obj[c.TimeSettings][c.TimeStartEFT])
        time_factor = c.obj[c.TimeSettings][c.TimeFactor]
        UpdateFrequency_ms = c.obj[c.TimeSettings][c.UpdateFrequency_ms]
        eft_time_instance = currenttime.EftTime(irl_start_time, eft_start_time, guiShown.time_1_label, guiShown.time_2_label, guiHidden.time_1_label, guiHidden.time_2_label, time_factor, UpdateFrequency_ms)
        
        gui_interact = GuiInteract(root, rootHidden, guiShown, eft_time_instance) 

        f.toggle_show_hide(root, c)
        
        if (c.obj[c.HotkeyConfig][c.HotkeysActive] == "True" or c.obj[c.HotkeyConfig][c.HotkeysActive] == "true"):
            logger.info("HotkeysActive:", c.obj[c.HotkeyConfig][c.HotkeysActive])
            activate_hotkeys(root, rootHidden, guiShown, gui_interact)

        root.mainloop()


def activate_hotkeys(root, rootHidden, guiShown, gui_interact): 
    logger.debug("Enter")
    x = threading.Thread(target=hotkeys.Hotkeys, args=(root, rootHidden, guiShown, gui_interact, c))
    x.daemon = True  # .daemon = closes the thread when no non-daemon is up
    x.start()
            
#def deactivate_hotkeys(): # Not implemented 
#    logger.debug("Enter")
#    pass


        
########## GUI

class RootHidden(tk.Tk):       ### HIDDEN
    logger.debug("Enter")
    def __init__(self):
        logger.debug("Enter")
        tk.Tk.__init__(self)
        self.attributes('-alpha', 0.0)
        self.lower()
        #self.iconify()
        self.title(c.obj[c.Gui][c.WindowName])#('TarkovTime')
        
        f.screen_placement(self, c, False) 

class RootShown(tk.Toplevel): ### SHOWN
    logger.debug("Enter")
    def __init__(self, master):
        logger.debug("Enter")
        tk.Toplevel.__init__(self, master)
        self.overrideredirect(1)

        
        f.screen_placement(self, c, False) 
        
        if (c.obj[c.General][c.RightClickToQuit] == "True" or c.obj[c.General][c.RightClickToQuit] == "true" ):
            self.bind('<ButtonRelease-3>', self.on_close)  #right-click to get out

    def on_close(self, event):
        logger.debug("Enter")
        self.master.destroy()

    
    

class GuiInteract(tk.Frame):
    logger.debug("Enter")
    def __init__(self, root, rootHidden, guiShown, eft_time_instance):
        logger.debug("Enter")
        tk.Frame.__init__(self,parent=None)
        #self.windowLocation_x = "WL_x"
        #self.windowLocation_y = "WL_y"
        #guiShown.time_1_label.bind("<Button-1>", lambda event, arg=root: self.get_window_location(event, arg)) #, windowLocation_x, windowLocation_y
        #guiShown.time_2_label.bind("<Button-1>", lambda event, arg=root: self.get_window_location(event, arg))

        
        if (c.obj[c.General][c.DragAnywhereToMove] == "True" or c.obj[c.General][c.DragAnywhereToMove] == "true"):
            guiShown.time_1_label.bind("<B1-Motion>", lambda event, arg=root: self.move_app(event, arg, rootHidden))
            guiShown.time_2_label.bind("<B1-Motion>", lambda event, arg=root: self.move_app(event, arg, rootHidden))

        guiShown.time_1_label.bind('<Double-Button-1>', lambda event, arg=root: self.open_config_menu(event, arg, guiShown, eft_time_instance))
        guiShown.time_2_label.bind('<Double-Button-1>', lambda event, arg=root: self.open_config_menu(event, arg, guiShown, eft_time_instance))
        
        if (c.obj[c.General][c.StartWithMenuOpen] == "True" or c.obj[c.General][c.StartWithMenuOpen] == "true"):
            self.open_config_menu(self, root, guiShown, eft_time_instance)

    
    def open_config_menu(self, e, root, guiShown, eft_time_instance):
        logger.debug("Enter")
        try: 
            if(self.labelframe_menu): 
                logger.debug("Config menu created before --> Closing old one and opening new")
                #self.labelframe.pack_forget()
                self.close_time_config()
                #return
        except: 
            logger.debug("Config menu never opened before --> Opening")
            
        _half_width = guiShown.time_1_label.winfo_width()//8    # .winfo_reqwidth()
        
        self.labelframe_menu = tk.LabelFrame(root, bd=0, highlightthickness=0, borderwidth=0, bg=c.obj[c.Gui][c.BackgroundColor], highlightcolor="black") #, height=100
        self.labelframe_menu.grid(row=2, column=0, columnspan=2)
        self.labelframe_menu.columnconfigure(0,weight=1, uniform='uniform')
        self.labelframe_menu.columnconfigure(1,weight=1, uniform='uniform')
        
        self.labelframe_left = tk.LabelFrame(self.labelframe_menu, bd=0, highlightthickness=0, borderwidth=0, bg=c.obj[c.Gui][c.BackgroundColor], highlightcolor="black") #, height=100
        self.labelframe_left.grid(row=0, column=0, columnspan=1, sticky=tk.NW)
        leftestTime_text = tk.StringVar()
        leftestTime_entry = tk.Entry(self.labelframe_left, textvariable=leftestTime_text, width=_half_width, fg=c.obj[c.Gui][c.FontColor]) 
        leftestTime_entry.insert(0, eft_time_instance.eft_start_time.strftime("%H:%M:%S")) # todaysDate = dt.datetime.now().strftime("%H:%M:%S") %H:%M:%S
        leftestTime_entry.grid(row=0, column=0, columnspan=5, sticky="W")

        
        save_button = tk.Button(self.labelframe_left, text="Save", command= lambda: self.save_time_config(leftestTime_text, eft_time_instance))
        save_button.grid(row=1, column=0, sticky="W") # , sticky="E"
        close_button = tk.Button(self.labelframe_left, text="Close", command=self.close_time_config)
        close_button.grid(row=1, column=1, sticky="W") # , sticky="W"

        self.labelframe_right = tk.LabelFrame(self.labelframe_menu, bd=0, highlightthickness=0, borderwidth=0, bg=c.obj[c.Gui][c.BackgroundColor], highlightcolor="black") #, height=100
        self.labelframe_right.grid(row=0, column=1)
        hide_button = tk.Button(self.labelframe_right, text="Hide", command=self.close_time_config)
        hide_button.grid(row=0, column=1, sticky="W")#side = "left", anchor=N, fill="x", expand="yes"
        quit_button = tk.Button(self.labelframe_right, text="Quit", command= lambda: self.quitter(root))
        quit_button.grid(row=0, column=2, sticky="W")# side = "right", anchor=N
        save_placement_button = tk.Button(self.labelframe_right, text="Save placement", command=lambda: self.save_screen_placement()) #, side = "bottom" side = "bottom", fill="x"
        save_placement_button.grid(row=1, column=1, columnspan=5)
        
        #self.disable_enable_hotkeys_button = tk.Button(self.labelframe_right, text="Disable Hotkeys", command=lambda: self.activate_deactivate_hotkeys(self))
        #self.disable_enable_hotkeys_button.grid(row=2, column=1, columnspan=5)
        
        self.key_pressed_label = tk.Label(self.labelframe_right, fg = c.obj[c.Gui][c.FontColor], bg = c.obj[c.Gui][c.BackgroundColor], font=c.obj[c.Gui][c.FontAndSize])
        self.key_pressed_label.config(text=str(""))
        self.key_pressed_label.config(font=11)
        self.key_pressed_label.grid(row=3, column=1, columnspan=5)
        
        
        #if(c.obj[c.HotkeyConfig][c.HotkeysActive] == "True" or c.obj[c.HotkeyConfig][c.HotkeysActive] == "true"): 
        #    self.disable_enable_hotkeys_button.config(text=str("Enable Hotkeys"))

    
    #def activate_deactivate_hotkeys(e, self): 
    #    logger.debug("Enter")
    #    btn_text= self.disable_enable_hotkeys_button['text']  # self.cget('text') btn['text'] 
    #    if(btn_text == "Enable Hotkeys"):
    #        self.disable_enable_hotkeys_button['text'] = "Disable Hotkeys"
    #    if(btn_text == "Disable Hotkeys"):
    #        self.disable_enable_hotkeys_button['text'] = "Enable Hotkeys"
            
    def save_screen_placement(self):
        logger.debug("Enter")
        c.obj[c.ScreenPlacement][c.ScreenPlacement_x] = c.obj[c.ScreenPlacement][c.ScreenPlacement_x_Temp] 
        c.obj[c.ScreenPlacement][c.ScreenPlacement_y] = c.obj[c.ScreenPlacement][c.ScreenPlacement_y_Temp] 
        readwriteconfig.write_config_screen_placement(c.obj)
    def save_time_config(self, leftestTime_text, eft_time_instance): 
        logger.debug("Enter")
        c.obj = readwriteconfig.write_config_time(leftestTime_text)
        eft_time_instance.irl_start_time = f.to_time_format(c.obj[c.TimeSettings][c.TimeStartIRL])
        eft_time_instance.eft_start_time = f.to_time_format(c.obj[c.TimeSettings][c.TimeStartEFT])
    def close_time_config(self, ): 
        logger.debug("Enter")
        self.labelframe_menu.grid_forget() #.destroy() #.pack_forget()
    #def get_window_location(self, e, root): 
    #    logger.debug("Enter")
    #    self.windowLocation_x = e.x_root
    #    self.windowLocation_y = e.y_root
    def move_app(self, e, root, rootHidden): # f.screen_placement(GUIHIDDEN, c, False) 
        #logger.debug("Enter")
        x = e.x_root - e.x
        y = e.y_root - e.y
        c.obj[c.ScreenPlacement][c.ScreenPlacement_x_Temp] = str(x)
        c.obj[c.ScreenPlacement][c.ScreenPlacement_y_Temp] = str(y)
        
        if (c.obj[c.General][c.DragAnywhereToMove] == "True" or c.obj[c.General][c.DragAnywhereToMove] == "true"):
            root.geometry(f'+{e.x_root}+{e.y_root}')
            rootHidden.geometry(f'+{e.x_root}+{e.y_root}')
        if (c.obj[c.General][c.AutosaveScreenPlacement] == "True" or c.obj[c.General][c.AutosaveScreenPlacement] == "true"):
            self.save_screen_placement()
    
    def quitter(e, root):
        logger.debug("Enter")
        root.quit()

class GuiThings():
    logger.debug("Enter")
    def __init__(self, root):
        logger.debug("Enter")
        root.config(bg = c.obj[c.Gui][c.BackgroundColor])
        self.labelframe = tk.LabelFrame(root, bd=0, highlightthickness=0, borderwidth=0, bg = c.obj[c.Gui][c.BackgroundColor], highlightcolor="black")
        self.labelframe.grid(row=0, column=0) 
        
        self.time_1_label = tk.Label(self.labelframe, fg = c.obj[c.Gui][c.FontColor], bg = c.obj[c.Gui][c.BackgroundColor], font=c.obj[c.Gui][c.FontAndSize]) # Bold # c.obj[c.Gui][c.BackgroundColor]
        self.time_2_label = tk.Label(self.labelframe, fg = c.obj[c.Gui][c.FontColor], bg = c.obj[c.Gui][c.BackgroundColor], font=c.obj[c.Gui][c.FontAndSize])
        
        
        
        self.time_1_label.grid(row=0, column=0, padx=15) 
        self.time_2_label.grid(row=0, column=1) 
        self.labelframe.columnconfigure(0, weight=1)
        if (c.obj[c.Gui][c.TransparentBackground] == "True" or c.obj[c.Gui][c.TransparentBackground] == "true"):
            root.attributes('-transparentcolor', c.obj[c.Gui][c.BackgroundColor])
        
        


if __name__ == "__main__":
    logger.debug("initiate main instance")
    main_instance = main()

