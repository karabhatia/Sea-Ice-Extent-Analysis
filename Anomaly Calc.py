import os
import pandas as pd


seaIce_df = pd.read_excel("C:\\Users\\AvgData\\Antarctic_avg.xlsx")

list_month=[]
for row in seaIce_df.itertuples(index=False):
    list_month.append([row.Jan, row.Feb, row.Mar, row.Apr, row.May, row.June, row.July, row.Aug, row.Sep, row.Oct, row.Nov, row.Dec])

#function for finding the average sea ice extent value for a month across various years
def yrmonavg(mon):
    sum=0
    for i in list_month:
        sum+=i[mon]
    avg_yr = sum/43
    return avg_yr


#function to calculate the anomaly for a given month
def anomcalc(mon):
    anom_list=[]
    for i in list_month:
        anom=i[mon]-yrmonavg(mon)
        anom_list.append(anom)
    return anom_list

yrlist=[]
for yrr in range(1980,2023):
        yrlist.append(yrr)

#appending this data into excel
df = pd.DataFrame ({'Years': yrlist, 'Jan': anomcalc(0), 'Feb': anomcalc(1), 'Mar': anomcalc(2), 'Apr': anomcalc(3), 'May': anomcalc(4),'June':anomcalc(5), 'July':anomcalc(6), 'Aug': anomcalc(7), 'Sep':anomcalc(8), 'Oct': anomcalc(9), 'Nov': anomcalc(10), 'Dec': anomcalc(11) })
df.to_excel('Antarctic_anomaly.xlsx')

