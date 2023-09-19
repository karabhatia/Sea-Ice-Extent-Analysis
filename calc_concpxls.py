import os
import pandas as pd
import rasterio
from datetime import date, timedelta
import openpyxl
from openpyxl import load_workbook
pixel_count_list = []

#function defining different percentages for different days of the year to calculate lower limit of concentration that passes off as sea ice.
def getPerc(days):
    high = 18
    if days <= 100:
        return 0
    elif days <= 200:
        return 0 + (13/100) * (days -100)
    elif days <=268:
        return 0 + (high/168) * (days - 100)
    elif 320 < days < 345:
        return 16 - (16 / (365 - 268)) * (days - 268)
    else:
        return 18 - (18/(365-268)) * (days - 268)

    # function for suming the total pixels that have sea ice concentration above a certain lower limit calculated based on what day of the year it is
def getPixCount(path, day_count):
    perc = getPerc(day_count)
    lower_pix = 152 + 848 * (perc/100)
    with rasterio.open(path) as dataset:
        conc = dataset.read(1)
        count = 0
        for row in conc:
            for px in row:
                if lower_pix < px <= 1000:
                    count += 1
    return(count)


#calculation of final sea ice extent for all the image files stored is some source_folder using the fuctions above and storing the values in a list
source_folder = "D:\\Sea Ice Concentration Data\\2003\\"
day_count = 0
obj1 = os.scandir(source_folder)
for entry1 in obj1:
    source_folder = "D:\\Sea Ice Concentration Data\\2003"
    if entry1.is_dir():
        source_folder = source_folder + "\\" + entry1.name
        obj2 = os.scandir(source_folder)
        for entry2 in obj2:
            if entry2.is_file():
                day_count += 1
                pixel_count_list.append((625*getPixCount(source_folder + "\\" + entry2.name, day_count)/1000000))


#storing all the data in day wise format in an excel file
date_year = []
date_month = []
date_date = []

start_date = date(2003, 1, 1)
end_date = date(2003, 12, 31)

delta = end_date - start_date   # returns timedelta

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    date_year.append(day.year)
    date_month.append(day.month)
    date_date.append(day.day)

df = pd.DataFrame ({'Years': date_year, 'Months': date_month, 'Day': date_date, 'Area': pixel_count_list})
df.to_excel('2003SIE.xlsx')
