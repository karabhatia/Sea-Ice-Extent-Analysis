import requests
import os
from bs4 import BeautifulSoup
#giving url of the year for which files have to be imported
url = "https://noaadata.apps.nsidc.org/NOAA/G02135/south/daily/geotiff/2009/"

r1 = requests.get(url)

htmlContent = r1.content
#getting all the data present in the page
soup1 = BeautifulSoup(htmlContent, 'html.parser')

for link1 in soup1.find_all("a"):
    output_folder = "D:\\NCPOR\\Sea Ice Concentration Data\\2009\\"
    href1 = link1.get("href")

    #looking for the right image files to dowload
    if href1.find("..") < 0:
        output_folder = output_folder + href1[0:6]
        href1=url + "/" + href1
        r = requests.get(href1)
        soup = BeautifulSoup(r.content, 'html.parser')

        #appending the urls of the required image files into a list
        file_links = []
        for link in soup.find_all("a"):
            href = link.get("href")
            if href.find("concentration_v3.0") > -1:
                file_links.append(href)

        #storing these files in the desired folder
        for file_link in file_links:
            file_url = href1 + "/" + file_link
            file_name = file_link.split("/")[-1]
            file_path = os.path.join(output_folder, file_name)
            response = requests.get(file_url)
            with open(file_path, "wb") as file:
                file.write(response.content)
