# -*- coding: utf-8 -*-

import csv
import os

data_dir = os.path.dirname(os.path.abspath(__file__))


class Check_date:
    
    def check_miladi_Hijri(self,data,row):
        if (data[0] == row[1]) and (data[1] in row[2]) and (data[2] in row[4]):
            return True
        if (data[0] == row[6]) and (data[1] in row[7]) and (data[2] in row[9]):
            return True    
        if (data[0] == row[11]) and (data[1] in row[12]) and (data[2] in row[14]):
            return True       



class Error_handle:
    
    def error_handel(self,err):#-
        """ 1 = Input date is incorrect
            2 = Date is not valid
             
        """
        if err == 1:
            return "error in input data "
        elif err == 2:
            return "date not valid"
        


class Jalali_import:

    def jalali_search(self,data_split,im_month,im_day,im_rtl):
        # The final return variable in the form of a tuple
        export_fjfm = ()
        all_ = data_split
        with open(data_dir+'/data/taghvim_db.csv','r',encoding="utf8") as db:
            file_read = csv.reader(db) 
            next(file_read)
            for _ in file_read:
                if Check_date().check_miladi_Hijri(all_,_):
                    export_fjfm = (_[11],)
                    if im_month == True:
                        export_fjfm = export_fjfm + (_[13],)
                    else:
                        export_fjfm = export_fjfm + (_[12],)
                    export_fjfm = export_fjfm + (_[14],)    
                    if im_day == True:
                        export_fjfm = export_fjfm + (_[15],)
                    if im_rtl == True:
                        return export_fjfm
                    else:
                        export_fjfm = export_fjfm[::-1]
                        return export_fjfm                    
            if export_fjfm == (""):
                return Error_handle().error_handel(2)
    
    def today_date(self,date_split):
        # The final return variable in the form of a tuple
        export_fjfm = ()
        all_ = date_split
        with open(data_dir+'/data/taghvim_db.csv','r',encoding="utf8") as db:
            file_read = csv.reader(db) 
            next(file_read)
            for _ in file_read:
                if Check_date().check_miladi_Hijri(all_,_):
                    export_fjfm = _[11]+"-"+_[12]+"-"+_[14]
                    return export_fjfm
    
    def range_jalali_data(self,inp_data,count,to_jalali,event,holiday,to_hejri):
        export_fjfm = ()
        all_data = []
        start_count = False
        all_ = inp_data
        with open(data_dir+'/data/taghvim_db.csv','r',encoding="utf8") as db:
            file_read = csv.reader(db) 
            next(file_read)
            _count_break = 0
            for _ in file_read:
                if Check_date().check_miladi_Hijri(all_,_):
                    start_count = True
                if start_count == True:
                    if to_jalali == True:
                        export_fjfm = (_[11],_[12],_[14],)
                    if holiday == True:
                        export_fjfm = export_fjfm + (_[16],)    
                    if event == True:
                        export_fjfm = export_fjfm + (_[17],)
                    if to_hejri == True:
                        export_fjfm = export_fjfm + (_[6],_[7],_[9],)                    
                    all_data.append(export_fjfm)
                    export_fjfm = ()
                    _count_break += 1 
                if _count_break >= count:
                    return all_data
            if export_fjfm == ():
                return Error_handle().error_handel(2)
         
         
        
class Gregorian_import:
    
    def gregorian_search(self,data_split,im_month,im_day,im_rtl):
        # The final return variable in the form of a tuple
        export_fjfm = ()
        all_ = data_split
        with open(data_dir+'/data/taghvim_db.csv','r',encoding="utf8") as db:
            file_read = csv.reader(db) 
            next(file_read)
            for _ in file_read:
                if Check_date().check_miladi_Hijri(all_,_):
                    export_fjfm = (_[1],)
                    if im_month == True:
                        export_fjfm = export_fjfm + (_[3],)
                    else:
                        export_fjfm = export_fjfm + (_[2],)
                    export_fjfm = export_fjfm + (_[4],)    
                    if im_day == True:
                        export_fjfm = export_fjfm + (_[5],)
                    if im_rtl == True:
                        return export_fjfm
                    else:
                        export_fjfm = export_fjfm[::-1]
                        return export_fjfm
            if export_fjfm == ():
                return Error_handle().error_handel(2) 
            
    def range_gregorian_data(self,inp_data,count,to_gregorian,event,holiday,to_hejri):
        export_fjfm = ()
        all_data = []
        start_count = False
        all_ = inp_data
        with open(data_dir+'/data/taghvim_db.csv','r',encoding="utf8") as db:
            file_read = csv.reader(db) 
            next(file_read)
            _count_break = 0
            for _ in file_read:
                if Check_date().check_miladi_Hijri(all_,_):
                    start_count = True
                if start_count == True:
                    if to_gregorian == True:
                        export_fjfm = (_[1],_[2],_[4],)
                    if holiday == True:
                        export_fjfm = export_fjfm + (_[16],)    
                    if event == True:
                        export_fjfm = export_fjfm + (_[17],)
                    if to_hejri == True:
                        export_fjfm = export_fjfm + (_[6],_[7],_[9],)                    
                    all_data.append(export_fjfm)
                    export_fjfm = ()
                    _count_break += 1 
                if _count_break >= count:
                    return all_data
            if export_fjfm == ():
                return Error_handle().error_handel(2)            
        
class Hijri_import:
    
    def hijri_search(self,data_split,im_month,im_day,im_rtl):
        # The final return variable in the form of a tuple
        export_fjfm = ()
        all_ = data_split
        with open(data_dir+'/data/taghvim_db.csv','r',encoding="utf8") as db:
            file_read = csv.reader(db) 
            next(file_read)
            for _ in file_read:
                if Check_date().check_miladi_Hijri(all_,_):
                    export_fjfm = (_[6],)
                    if im_month == True:
                        export_fjfm = export_fjfm + (_[8],)
                    else:
                        export_fjfm = export_fjfm + (_[7],)
                    export_fjfm = export_fjfm + (_[9],)    
                    if im_day == True:
                        export_fjfm = export_fjfm + (_[10],)
                    if im_rtl == True:
                        return export_fjfm
                    else:
                        export_fjfm = export_fjfm[::-1]
                        return export_fjfm                    
            if export_fjfm == ():
                return Error_handle().error_handel(2) 
        
    def today_date(self,date_split):
        # The final return variable in the form of a tuple
        export_fjfm = ()
        all_ = date_split
        with open(data_dir+'/data/taghvim_db.csv','r',encoding="utf8") as db:
            file_read = csv.reader(db) 
            next(file_read)
            for _ in file_read:
                if Check_date().check_miladi_Hijri(all_,_):
                    export_fjfm = _[6]+"-"+_[7]+"-"+_[9]
                    return export_fjfm            
