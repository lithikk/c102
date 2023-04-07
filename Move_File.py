import os
import shutil



source="C:/Users/santh/Downloads"
destination="C:/Users/santh/OneDrive/Desktop/Document_Files"
list_of_files = os.listdir(source)
#print(list_of_files)
for i in list_of_files:
    name,extension=os.path.splitext(i)
    if extension=="":
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1=source + "/" + i 
        path2=destination + "/" + "docfiles"
        path3=destination + "/" + "docfiles" + "/" + i    


        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3) 
