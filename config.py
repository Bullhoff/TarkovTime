from loguru import logger
logger.debug("Enter module")

from configparser import ConfigParser



class TestClass():     
    logger.debug("Enter")
    ShowHide = ""
    
    ##########  NameUsedInCode = NameInConfigFile
    #####
    General = "General" #####   General
    LoggerLevel = "__NotImplemented__LoggerLevel"
    SaveLog = "__NotImplemented__savelog"
    AutosaveScreenPlacement = "AutosaveScreenPlacement"
    RightClickToQuit = "RightClickToQuit"
    DragAnywhereToMove = "DragAnywhereToMove"
    StartWithMenuOpen = "startwithmenuopen"
    
    Gui = "Gui" #####   GUI
    WindowName = "windowname"
    FontColor = "FontColor"
    FontAndSize = "FontAndSize"
    BackgroundColor = "BackgroundColor"
    TransparentBackground = "TransparentBackground"
    HighlightColor = "HighlightColor"
    
    TimeSettings = "TimeSettings"   #####   TimeSettings
    TimeStartIRL = "TimeStartIRL"
    TimeStartEFT = "TimeStartEFT"
    TimeFactor = "TimeFactor"
    UpdateFrequency_ms = "UpdateFrequency_ms"
    FileorAPI = "__NotImplemented__FileorAPI"
    
    ScreenPlacement = "ScreenPlacement" #####   ScreenPlacement
    ScreenPlacement_x = "ScreenPlacement_x"
    ScreenPlacement_y = "ScreenPlacement_y" 
    ScreenPlacement_x_Temp = "ScreenPlacement_x_Temp"
    ScreenPlacement_y_Temp = "ScreenPlacement_y_Temp"
        
    HotkeyConfig = "__NotImplemented__HotkeyConfig"   #####   HotkeyConfig
    HotkeysActive = "HotkeysActive"
    ShowBackgroundDuration = "ShowBackgroundDuration_s"
    
    Hotkeys = "__NotImplemented__Hotkeys" #####   Hotkeys
    KeyExamples = "__KeyExamples"
    ShowBackground = "showbackground" 
    HideShowTarkovTime = "hideshowtarkovtime"
    ToggleAlwaysOnTop = "ToggleAlwaysOnTop"
    ExitTarkovTime = "exittarkovtime"
    MoveToCenter = "movetocenter"
    
    config_object = ConfigParser()
    config_object[General] = {
        #LoggerLevel: "INFO", #"DEBUG", 
        #SaveLog: "False", 
        AutosaveScreenPlacement: "False", 
        RightClickToQuit: "True", 
        DragAnywhereToMove: "True", 
        StartWithMenuOpen: "True"
        
    }
    config_object[Gui] = {
        WindowName: "TarkovTime",
        FontColor: "Green",
        FontAndSize: "Helvetica 18",
        BackgroundColor: "Black", 
        TransparentBackground:"True", 
        HighlightColor: "gray"
        
    }
    config_object[TimeSettings] = {
        TimeStartIRL: "2022-10-01 17:52:56",
        TimeStartEFT: "2022-10-01 18:10:30",
        TimeFactor: "7", 
        UpdateFrequency_ms: "142",
        FileorAPI: "File"
    }
    config_object[ScreenPlacement] = {
        ScreenPlacement_x: "", 
        ScreenPlacement_y: "", 
        ScreenPlacement_x_Temp: "", 
        ScreenPlacement_y_Temp: ""
    }
    config_object[HotkeyConfig] = {
        HotkeysActive: "False",
        ShowBackgroundDuration : "2"
    }
    config_object[Hotkeys] = {
        KeyExamples: "Num3(<99>), Num2(<98), Num4(<100>), page_down, page_up", 
        
        ShowBackground: "<99>",
        HideShowTarkovTime: "<97>", 
        #ToggleAlwaysOnTop: "___",
        ExitTarkovTime: "<100>", 
        MoveToCenter: "<98>"
    }
    obj = config_object