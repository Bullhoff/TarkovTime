import datetime as dt
from loguru import logger
logger.debug("Enter module")

def ___now_formatted(): 
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return now
def ___add_date_time(time):
    todaysDate = dt.datetime.now().strftime("%Y-%m-%d")
    temp = leftestTime_entry.get()
    leftestTime = str(todaysDate) + " " + str(temp)
def __get_logger():
    from loguru import logger
    #logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
    logger.debug("get_logger")
    return logger
  


def to_time_format(date_and_time):
    logger.debug("Enter")
    return dt.datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S")
    
def screen_placement(self, c, go_to_center):
    logger.debug("Enter. go_to_center:{}", go_to_center)
    if(c.obj[c.ScreenPlacement][c.ScreenPlacement_x] and not go_to_center):
        screen_placement_from = "ConfigFile"
        screen_placement_x = c.obj[c.ScreenPlacement][c.ScreenPlacement_x]
        screen_placement_y = c.obj[c.ScreenPlacement][c.ScreenPlacement_y]
    if not(c.obj[c.ScreenPlacement][c.ScreenPlacement_x]) or go_to_center:
        screen_placement_from = "Monitor/2"
        screen_width = self.winfo_screenwidth()
        screen_width_half = screen_width//2
        screen_height = self.winfo_screenheight()
        screen_height_half = screen_height//2
        
        screen_placement_x = screen_width_half
        screen_placement_y = screen_height_half #150
            
    screen_placement_xy = '+'+str(screen_placement_x)+'+'+str(screen_placement_y)
    logger.debug("screen_placement :{}   *From:{}", screen_placement_xy, screen_placement_from)
    self.geometry(screen_placement_xy)
    
    
def toggle_show_hide(root, c): 
    logger.debug("Enter")
    if (c.ShowHide == "Show"):
        logger.debug("Show --> Hide")
        root.attributes('-topmost', 0)
        root.lower()
        c.ShowHide = "Hide"
    else: 
        logger.debug("Hide --> Show")
        root.attributes('-topmost', 1)
        c.ShowHide = "Show"
        
    
    
def destroy(root): 
    logger.debug("Enter")
    root.destroy()



    
