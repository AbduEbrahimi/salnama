# -*- coding: utf-8 -*-

import csv
import datetime
import os
from .taghvim_import import Gregorian_import
from .taghvim_import import Jalali_import
from .taghvim_import import Hijri_import
from .taghvim_import import Error_handle
from .taghvim_import import Check_date

jalali_im = Jalali_import()
gregorian_im = Gregorian_import()
hijri_im = Hijri_import()
error = Error_handle()
check = Check_date()
data_dir = os.path.dirname(os.path.abspath(__file__))



#-----------------------jalali----------------------
class Jalali:
               
    def holiday(self,holyday_date):
        """ Inquiry about the day off from the date
            , holyday_date = str(data) : "2020-3-20"
        """
        holiday_time = holyday_date.split("-")
        if len(holiday_time) == 3:        
            export_holiday = ""
            with open(data_dir+'/data/taghvim_db.csv','r',encoding="utf8") as db:
                file_read = csv.reader(db) 
                next(file_read)
                for _ in file_read:
                    if check.check_miladi_Hijri(holiday_time,_):
                        export_holiday = _[16]        
                        return export_holiday                        
                if export_holiday == "":
                    return error.error_handel(2)
        else:
            return error.error_handel(1)                        
			
    def event(self,event_date):
        """ Inquiry for one day event
            , event_date = str(data) : "2020-3-20"
        """
        event_time = event_date.split("-")        
        if len(event_time) == 3:
            event_export = ""
            with open(data_dir+'/data/taghvim_db.csv','r',encoding="utf8") as db:
                file_read = csv.reader(db) 
                next(file_read)            
                for _ in file_read:
                    if check.check_miladi_Hijri(event_time,_):
                        event_export = _[17]        
                        return event_export
                if event_export == "":
                    return error.error_handel(2)
        else:
            return error.error_handel(1)         
    
    def range(self,in_date,count,to_jalali=True,holiday=False,event=False,to_hejri=False):
        #Convert a variable to a date
        in_date = in_date.split("-")
        # Validity of date to year, month and day
        if len(in_date) == 3 and count == int(count) and count > 0 : 
            range_jalali = jalali_im.range_jalali_data(in_date,count,to_jalali,event,holiday,to_hejri)
            return range_jalali
        else:
            return error.error_handel(1)
    
    def find_(self,find_date,month=False,day=False,rtl=True):
        """  find_date : str(date) : "2020-3-20"
            , month : Show month name  
            , day : Show names per week
            , rtl : Right to left
        """
        #Convert a variable to a date
        all_time = find_date.split("-")
        # Validity of date to year, month and day
        if len(all_time) == 3: 
            jalali_find = jalali_im.jalali_search(all_time,month,day,rtl)
            return jalali_find
        else:
            return error.error_handel(1)

    def today(self,to_list=False):
        utc_date = datetime.datetime.now(datetime.timezone.utc)
        utc_tuple = utc_date.timetuple()
        date_split = (str(utc_tuple[0]),str(utc_tuple[1]),str(utc_tuple[2]))
        result = jalali_im.today_date(date_split)
        if to_list == False:
            return result    
        else:
            new_result = result.split("-")
            return new_result        
        
    def tomorow(self,to_list=False):
        now_date = datetime.datetime.now(datetime.timezone.utc)
        tomorow_date = now_date + datetime.timedelta(days=1)
        tomorow_list = tomorow_date.timetuple()
        tomorow_splite = str(tomorow_list[0])+"-"+str(tomorow_list[1])+"-"+str(tomorow_list[2])
        if to_list == False:
            jalali_date_list = list(self.find_(tomorow_splite))
            jalali_tomorow = jalali_date_list[0]+"-"+jalali_date_list[1]+"-"+jalali_date_list[2]
            return jalali_tomorow
        else:
            jalali_tomorow = list(self.find_(tomorow_splite))
        return jalali_tomorow
    
class Gregorian:
    
    def find_(self,find_date,month=False,day=False,rtl=False):
        """  find_date : str(date) : "1399-1-1"
            , month : Show month name  
            , day : Show names per week
            , rtl : Right to left
        """
        #Convert a variable to a date
        all_time = find_date.split("-")
        # Validity of date to year, month and day
        if len(all_time) == 3: 
            gregorian_find = gregorian_im.gregorian_search(all_time,month,day,rtl)
            return gregorian_find
        else:
            return error.error_handel(1)    
        
    def range(self,in_date,count,to_gregorian=True,holiday=False,event=False,to_hejri=False):
        #Convert a variable to a date
        in_date = in_date.split("-")
        # Validity of date to year, month and day
        if len(in_date) == 3 and count == int(count) and count > 0 : 
            range_jalali = gregorian_im.range_gregorian_data(in_date,count,to_gregorian,event,holiday,to_hejri)
            return range_jalali
        else:
            return error.error_handel(1)       
        
    def today(self,to_list=False):
        utc_date = datetime.datetime.now(datetime.timezone.utc)
        utc_tuple = utc_date.timetuple()
        date_split = str(utc_tuple[0])+"-"+str(utc_tuple[1])+"-"+str(utc_tuple[2])
        if to_list == False:
            return date_split
        else:
            new_result = date_split.split("-")
            return new_result                   

    def tomorow(self,to_list=False):
        now_date = datetime.datetime.now(datetime.timezone.utc)
        tomorow_date = now_date + datetime.timedelta(days=1)
        tomorow_list = tomorow_date.timetuple()
        tomorow_splite = str(tomorow_list[0])+"-"+str(tomorow_list[1])+"-"+str(tomorow_list[2])
        if to_list == False:
            return tomorow_splite
        else:
            tomorow_gregorian = [str(tomorow_list[0]),str(tomorow_list[1]),str(tomorow_list[2])]
            return tomorow_gregorian

class Hijri:
    
    def find_(self,find_date,month=False,day=False,rtl=True):
        """  find_date : str(date) = "1399-1-1" or "2020-3-20"
            , month : Show month name  
            , day : Show names per week
            , rtl : Right to left
            
        """
        #Convert a variable to a date
        all_time = find_date.split("-")
        # Validity of date to year, month and day
        if len(all_time) == 3: 
            hijri_find = hijri_im.hijri_search(all_time,month,day,rtl)
            return hijri_find
        else:
            return error.error_handel(1)        
        
    def today(self,set_hijri=0,to_list=False):
        utc_date = datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(days=set_hijri)
        utc_tuple = utc_date.timetuple()
        date_split = (str(utc_tuple[0]),str(utc_tuple[1]),str(utc_tuple[2]))
        result = hijri_im.today_date(date_split)
        if to_list == False:
            return result    
        else:
            new_result = result.split("-")
            return new_result

    def tomorow(self,set_hijri=0,to_list=False):
        now_date = datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(days=set_hijri)
        tomorow_date = now_date + datetime.timedelta(days=1)
        tomorow_list = tomorow_date.timetuple()
        tomorow_splite = str(tomorow_list[0])+"-"+str(tomorow_list[1])+"-"+str(tomorow_list[2])
        hijri_date_list = list(self.find_(tomorow_splite))
        if to_list == False:
            hijri_tomorow = hijri_date_list[0]+"-"+hijri_date_list[1]+"-"+hijri_date_list[2]
            return hijri_tomorow
        else:
            return hijri_date_list    
