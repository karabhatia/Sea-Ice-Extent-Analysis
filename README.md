# Sea-Ice-Extent-Analysis
The program was written to collect and traverse sea ice extent data in the Antarctic region and the processed data was used for mapping out sea ice extent trends and the factors affecting it.

## Usage
The program used data from the following site for calculation of sea ice extent : https://noaadata.apps.nsidc.org/NOAA/G02135/south/daily/

Inorder to run the program for a different tif image based data set, 
Go to scrapetifconc.py and change the following line
```python
#scrapetifconc.py

...
    url = "GIVE_YOUR_URL"
...

```
To store the data in the desired folders make the following changes in scrapetifconc.py
```python
#scrapetifconc.py

...
    output_folder = "PATH_OF_YOUR_FOLDER"
    href1 = link1.get("href")
...
```

Make following path changes in the respective files to direct the program to the place where your data is stored
```python
#calc_concpxls.py
...
    source_folder = "PATH_OF_THE_FOLDER_WHERE_SCRAPED_IMAGE_FILES_ARE_STORED"
...

#Monthavg.py
...
    seaIce_df = pd.read_excel("PATH_OF_EXCEL_FILE_WHERE_SIE_DATA_IS_STORED")
...

#Anomaly Calc.py
...
    seaIce_df = pd.read_excel("PATH_OF_EXCEL_FILE_WHERE_AVG_DATA_IS_STORED")
...

```
To store the processed data in desired excel files, specify file name in the following places in respective python files
```python

#calc_concpxls.py
...
     df.to_excel('NAME_OF_YOUR_EXCEL_FILE')
...

#Monthavg.py
...
    df.to_excel('NAME_OF_YOUR_EXCEL_FILE')
...

#Anomaly Calc.py
...
    df.to_excel('NAME_OF_YOUR_EXCEL_FILE')
...

```

## Limitaions
Limitations are listed as below. 

1. The program is designed to run for image files with tif extention
2. The final anomaly data set generated has been presented in a format that helps with correlation of data with only certain types of local and global geo indices.
