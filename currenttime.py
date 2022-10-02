from loguru import logger
logger.debug("Enter module")

import datetime as dt

class EftTime():
    logger.debug("Enter")
    #irl_start_time = dt.datetime(2021, 3, 16, 19, 21, 25)
    #eft_start_time = dt.datetime(2021, 3, 20, 11, 30, 00)
    
    def __init__(self, irl_start_time, eft_start_time, time_1_label, time_2_label, time_1_label_hidden, time_2_label_hidden, time_factor, UpdateFrequency_ms):
        logger.debug("Enter")

        self.irl_start_time = irl_start_time
        self.eft_start_time = eft_start_time
        self.time_factor = int(time_factor)

        def tick():
            self.irl_datetime_difference = self.getDateTimeDifference(self.irl_start_time)
            self.timedate_1 = self.getEftTime(self.eft_start_time, self.irl_datetime_difference, self.time_factor)
            self.timedate_2 = self.timedate_1 + dt.timedelta(hours = 12)
            self.time_1 = self.timedate_1.strftime("%H:%M:%S")
            self.time_2 = self.timedate_2.strftime("%H:%M:%S")
            time_1_label.config(text=str(self.time_1))
            time_2_label.config(text=str(self.time_2))
            
            time_1_label_hidden.config(text=str(self.time_1))
            time_2_label_hidden.config(text=str(self.time_2))

            time_1_label.after(UpdateFrequency_ms,tick)
        tick()


    def getDateTimeDifference(self, then):
        #logger.debug("Enter")
        self.now = dt.datetime.now()
        self.difference = self.now - then
        return self.difference

    def getEftTime(self, then, difference, time_factor):
        #logger.debug("Enter")
        self.now = then + difference*time_factor #7
        return self.now
    