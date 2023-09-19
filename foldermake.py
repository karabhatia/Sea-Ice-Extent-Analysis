import os

#creating various folders by using the folder design of an old one
def recreate_folder_structure(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        target_path = os.path.join(target_folder, relative_path)
        os.makedirs(target_path, exist_ok=True)

source_folder = "D:\\SampleFolder"
for i in range(2008,2010):
    import os

    parent_folder = "D:\\NewFolders"
    new_folder_name = str(i)

    new_folder_path = os.path.join(parent_folder, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    recreate_folder_structure(source_folder, new_folder_path)
df = pd.DataFrame ({'Years': date_year, 'Months': date_month, 'Day': date_date, 'Area': pixel_count_list})
workbook = load_workbook("Test.xlsx")
writer = pd.ExcelWriter("Test.xlsx", engine= 'openpyxl')
writer.book = workbook
writer,sheets = {ws.title: ws for ws in workbook.worksheets}

df.to_excel(writer, startrow=writer.sheets['Sheet2'].max_row, index= False, header = False)
writer.close()