
import os,sys
def delete_files_by_name(filenametobedeleted = r'_vnote.json'):
    for foldname,subfolders,filenames in os.walk(path):
        for filename in filenames:
            if filename == filenametobedeleted:
                os.remove(os.path.join(foldname,filename))
                print("{} deleted.".format(filename))


if __name__ == 'main':
    path = r'C:\Users\HUMAN\Desktop\vnote_temp\vnote_notebooks' 
    # "C:\\Users\\HUMAN\\Desktop\\vnote_temp\\vnote_notebooks\\""
    delete_files_by_name(r'_vnote.json') #









































