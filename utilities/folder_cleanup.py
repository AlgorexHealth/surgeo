'''Delete all .uf1 and .zip files in folder.'''

import os

def folder_cleanup():
    # Created named tuple for organizing
    home_dir_path = os.path.expanduser("~")
    data_dir_path = os.path.join(home_dir_path, '.surgeo')     
    file_list = os.listdir(data_dir_path)
    for filename in file_list:
        if filename == 'census.db':
            continue
        if filename == 'configuration.txt':
            continue
        if filename == 'logo.jpg':
            continue
        os.remove(os.path.join(data_dir_path,
                               filename))
