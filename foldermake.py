import os
#creating various folders by using the folder design of an old one

#defining fuction for copying folder structure
def recreate_folder_structure(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        target_path = os.path.join(target_folder, relative_path)
        os.makedirs(target_path, exist_ok=True)
        
#a variable holding the path of the folder structure to be recreated
source_folder = "D:\\NCPOR\\Sea Ice Concentration Data\\2000"

#running loop for number of times this structure has to be replicated
for i in range(2008,2010):
    import os
    parent_folder = "D:\\NCPOR\\Sea Ice Concentration Data"
    new_folder_name = str(i)
    new_folder_path = os.path.join(parent_folder, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    recreate_folder_structure(source_folder, new_folder_path)
    
