import os, shutil
from_dir = "C:/Users/Arjun/Downloads"
to_dir = "C:/Users/Arjun/Desktop"
extensions = [".txt", ".doc", ".docx", ".pdf"]
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file in list_of_files:
    name,ext=os.path.splitext(file)
    print(file)
    if ext in extensions:
        path1 = from_dir+'/'+file
        path2 = to_dir+'/'+"Document_Files"
        path3 = to_dir+'/'+"Document_Files"+'/'+file
        if os.path.exists(path2):
            print("Moving"+file+".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving"+file+".....")
            shutil.move(path1,path3)

    
   