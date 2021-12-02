# This script should take a zipped folder and extract it to an output folder that is unzipped.
# This script should also print messages regarding completion.

def extractZipFile(input_folder_name, output_folder_name):
    # importing required modules
    from zipfile import ZipFile
    print('this script received: \n Input folder: ' + input_folder_name +'\nOutput folder: ' + output_folder_name)
    with ZipFile(input_folder_name, 'r') as zip:
        print('Extracting the following folders now...')
        print(zip.namelist())
        zip.extractall(output_file_name)
        print(output_file_name + '  is Done!\n')