 IMPORT THE LIBRARIES
import os
import shutil

#CREATE A VARIABLE TO STORE THE DIRECTORY PATH
path = input("ENTER THE DIRECTORY PATH WHICH YOU WANT TO BE SORTED")

#CREATE A VARIABLE WHICH WILL STORE THE LIST OF FILES IN THE DIRECTORY
list_of_files = os.listdir(path)

# RUN A FOR LOOP FOR SPLITING THE FILE ACCORDING TO THEIR EXTENSION
for file in list_of_files:
    name,ext = os.path.splitext(file)

    # CREATE THE EXTENSION FOLDER
    ext = ext[1:]

    if ext == '':
        continue

    #WRITE A CONDITION WHICH WILL SEPARATE THE FILES ACCORDING TO EXTENSION FOLDER WHICH ALREADY CREATES
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

    # ELSE WRITE A CONDITION FOR CREATEING A NEW EXTENSION FOLDER THEN SEPARATING THE FILES
    else :
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

