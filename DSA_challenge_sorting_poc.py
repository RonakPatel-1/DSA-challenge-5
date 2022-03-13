import os
import shutil
   
# Enter the folder/directory name which needs to be sorted
print("Welcome to DSA Challenege solution by Ronak Jitendrabhai Patel.. \n I tried very simple logic to sort the all file formats with different extension and creating a folder for each file format extension and moving the unstructed data into a structured one using python code \n")
path = input(" Please enter below folder full path with out any single or double quotations : \n")
  
  
# This will create a properly organized and structured list with all the filename that is there in the directory/Folder
list_ = os.listdir(path)
   
# It will go an iternate to each and every file
for file_ in list_:
    name, ext = os.path.splitext(file_)
  
    #  to store the extension type
    ext = ext[1:]
  
    # For next iteration  if it is the directory
    if ext == '':
        continue
  
    # This will move the file to the directory/folder  where the name 'ext' already exists
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
  
    # if the directory does not already exist then this will create a new folder/directory
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
print(" \n Go back to above entered folder and now the check the data looks very structured one \n")