import os
import pandas as pd

#reading the day wise data stored in excel
seaIce_df = pd.read_excel("C:\\Users\\Antarctic_SIE.xlsx")
sea_data = seaIce_df.loc[(seaIce_df.Months.isin([1,2,3,4,5,6,7,8,9,10,11,12]))]

#getting a count of days for which data is available
month_list=[]
for i in range(1980, 2023):
    data_sea = sea_data.loc[(sea_data['Years'] == i)]
    month_count = {}
    for num in range(1, 13):
        month_count[num] = 0
    for m in data_sea['Months']:
        month_count[m]+=1
    month_list.append(month_count)

list_alldays=[]

for row in seaIce_df.itertuples(index=False):
    list_alldays.append([row.Years, row.Months, row.Day, row.Area])

#total sea ice extent calculated for every month of every year
month_arlist=[]
for n in range(1980, 2023):
    month_arcount={}
    for mon in range(1,13):
        sum_area=0
        for elem in list_alldays:
            if elem[0]==n and elem[1]==mon:
                sum_area += elem[3]
        month_arcount[mon]=sum_area
    month_arlist.append(month_arcount)

#calculating monthly average sea ice extent and storing in a list with the year, the month and the averaged value.
avg_list=[]
for yr in range(43):

    for yrmon in range(1,13):
        monavg= month_arlist[yr][yrmon] / month_list[yr][yrmon]
        avg_list.append([1980+yr, yrmon, monavg])


yrlist=[]
for yrr in range(1980,2023):
        yrlist.append(yrr)

#function which returns the list of averages for every month across the years.
def avgdata(mon):
    data_mon=[]
    for elem in avg_list:
        if elem[1]==mon:
            data_mon.append(elem[2])
    return data_mon



#Inserting all the data in an excel file.
df = pd.DataFrame ({'Years': yrlist, 'Jan': avgdata(1), 'Feb': avgdata(2), 'Mar': avgdata(3), 'Apr': avgdata(4), 'May': avgdata(5),'June':avgdata(6), 'July':avgdata(7), 'Aug': avgdata(8), 'Sep':avgdata(9), 'Oct': avgdata(10), 'Nov': avgdata(11), 'Dec': avgdata(12) })

df.to_excel('Antarctic_avg.xlsx')





