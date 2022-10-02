from loguru import logger
logger.debug("Enter module")

from configparser import ConfigParser


import datetime as dt
import currenttime

configFileName = "config.ini"


def _parse_config(config_object_default, config_object_file):
    logger.debug("Enter")
    
    for section in config_object_default: 
        if not (config_object_file.has_section(section)): 
            config_object_file[section] = {} 
            
        
        logger.debug("--Checking Section: {}".format(section))    
        for option in config_object_default[section]: 
            logger.debug("---Checking Section: {}".format(option))  
            
            if not (config_object_file.has_option(section, option)): # or option == "" option == ""
                config_object_file[section][option] = ""
                logger.debug("----Created Option: {}".format(option))
                
            if not (config_object_file[section][option]):
                config_object_file[section][option] = config_object_default[section][option]
                logger.debug("-----Created Option: {} = {}".format(option, config_object_default[section][option]))
                
    
    return config_object_file


def read_config_file(config_object_current): 
    logger.debug("Enter")
        
    config_object_file = ConfigParser()
    config_object_file.read(configFileName) # config.ini
    
    config_object = ConfigParser()
    config_object = _parse_config(config_object_current, config_object_file)
    
    write_config_full(config_object)
    
    return config_object



def write_config_time(leftestTime_entry):
    logger.debug("Enter")
    #logging.info("Function:   write_config_time")
    config_object = ConfigParser()

    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    todaysDate = dt.datetime.now().strftime("%Y-%m-%d")
    temp = leftestTime_entry.get()
    leftestTime = str(todaysDate) + " " + str(temp)
    logger.info("Writing EFT time to Config: *Now: {} *Left EFT Time: {}", now, leftestTime)
    config_object.read(configFileName)
    config_object["TimeSettings"]["TimeStartIRL"] = now 
    config_object["TimeSettings"]["TimeStartEFT"] = leftestTime
    
    with open(configFileName, 'w') as conf: # config.ini
        config_object.write(conf)

    return config_object
    
def write_config(section, key, value):
    logger.debug("Enter")
    config_object = ConfigParser()
    config_object.read(configFileName)
    config_object[section][key] = value 
    
    with open(configFileName, 'w') as conf: # config.ini
        config_object.write(conf)

    return config_object

def write_config_screen_placement(config_object):
    logger.debug("Enter")
    with open(configFileName, 'w') as conf: # config.ini
        config_object.write(conf)

    return config_object

def write_config_full(config_object):
    logger.debug("Enter")
    with open(configFileName, 'w') as conf: # config.ini
        config_object.write(conf)

    return config_object

