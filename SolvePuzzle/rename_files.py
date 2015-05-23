import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\Rajesh\Documents\GitHub\PythonPortfolio\SolvePuzzle\prank\prank")
    #print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Rajesh\Documents\GitHub\PythonPortfolio\SolvePuzzle\prank\prank")

    #(2) for each file, rename filename
    for file_name in file_list:
        print ("Old file name: " + file_name)
        print ("New file name: " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
