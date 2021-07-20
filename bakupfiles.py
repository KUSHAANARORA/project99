import os
import shutil
import time
def main():
    deletedfilescount = 0
    deletedfoldercount = 0
    path = "bakupfiles"
    days = 30
    seconds = time.time() - (days*24*60*60)
    if(os.path.exists(path)):
        for root_folder,folders,files in os.walk(path):
            if(get_folder_or_file_age(root_folder)<=seconds):
                removefolder(root_folder)
                deletedfoldercount = deletedfoldercount + 1
                break
            else:
                for folder in folders:
                    folderpath = os.path.join(root_folder,folder)
                    if(get_folder_or_file_age(folderpath)<=seconds):
                        removefolder(folderpath)
                        deletedfoldercount = deletedfoldercount + 1
                for file in files:
                    filepath = os.path.join(root_folder,file)
                    if(get_folder_or_file_age(filepath)<=seconds):
                        removefile(filepath)
                        deletedfilecount = deletedfilecount + 1




def get_folder_or_file_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

def removefolder(path):
    if not shutil.rmtree(path):
        print("path has been removed succesfully")
    else:
        print("folder cannot be removed")

def removefile(path):
    if not os.remove(path):
        print("path has been removed succesfully")
    else:
        print("file cannot be removed")