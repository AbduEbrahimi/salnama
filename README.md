## salnama

#salnama is a Python(v3.x) library for Calendar and Date Convertor For Persian Date, Gregorian Date ,Arabian Date with holiday and Events


## تقویم ۵ ساله سالنما  

# امکانات 
از فروردین ۱۳۹۹ تا فروردین ۱۴۰۴ (۵ ساله) 
شامل روز های تعطیل و مناسبت ها

امکان تبدیل تاریخ میلادی به جلالی و برعکس

امکان تبدیل تاریخ جلالی به تاریخ هجری و برعکس

امکان تبدیل تاریخ میلادی به تاریخ هجری و برعکس

شامل نام روز ها و ماه ها به زبان های فارسی -لاتین -عربی

امکان جستجو مناسبت ها و تعطیلات چند روز آینده یا گذشته


## Installation

Use the package manager [pip](https://pypi.org/project/salnama) to install salnama
```bash
pip3 install salnama
or
python3 setup.py install
```

#Use only on Linux

## Usage

```python
>>> from salnama import taghvim
>>> jalali = taghvim.Jalali()
>>> jalali.today()
'1399-11-8'
>>> jalali.event(jalali.today())
'سالروز وفات حضرت امالبنین (س) - روز تکریم مادران و همسران شهدا'
>>> jalali.event('2024-3-27') # Gregorian Date
'روز جهانی تئاتر'
>>> jalali.event('1446-5-24') # Hijri Date
'زمین لرزه ی بم- سالروز شهادت آشو زرتشت- جشن کریسمس'
>>> calendar = jalali.find_('2020-1-27',month=True,day=True,rtl=False)
>>> calendar
('سه شنبه', '6', 'آبان', '1399')
>>> calendar[3]
'1399'
>>> jalali.holiday('1402-5-13')
'تعطیل'
>>> hijri = taghvim.Hijri()
>>> hijri.today()
'1442-6-13'
>>> hijri.today(-1)#Change the days of the month 
'1442-6-12'
>>>jalali.range('1402-1-1',6,to_jalali=True,holiday=True,event=False)
[('1402', '1', '1', 'تعطیل'),
 ('1402', '1', '2', 'تعطیل'),
 ('1402', '1', '3', 'تعطیل'),
 ('1402', '1', '4', 'تعطیل'), 
 ('1402', '1', '5', ''),
 ('1402', '1', '6', '')]
>>> miladi = taghvim.Gregorian()
>>> miladi.find_('1403-9-14')
('4', '12', '2024')
>>> miladi.find_('1403-9-14',rtl=True)
('2024', '12', '4')
```

## Contributing
Pull requests are welcome.

## License
[Apache License Version 2.0](http://www.apache.org/licenses/)
