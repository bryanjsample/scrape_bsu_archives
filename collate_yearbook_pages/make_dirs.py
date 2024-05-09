'''
    module.py
    Author : Bryan Sample

    Module to create subdirectories inside of src_path
'''

from typing import List
import os

def create_directories(src_path:str, yearbooks:List[int]) -> List[int]:
    '''
        Create directories for any years that do not already exist at the source path and returns them in a list.
        Arguments:
            - src_path : string | path to parent directory where sub-dirs will be made and images will be saved
            - yearbooks : list of integers | list of target years to scrape
    '''
    lsDir = os.listdir(src_path)
    good_years:List[int] = []
    for year in yearbooks:
        if str(year) in lsDir:
            print(f'Directory already exists for {year}.\n')
        elif year not in list(range(1957,1972)):
            print(f'{year} is not a valid year. Check your arguments.')
        else:
            good_years.append(year)
            #for each year, create these dirs
            os.mkdir(f'{src_path}/{year}')
            os.mkdir(f'{src_path}/{year}/images')
            os.mkdir(f'{src_path}/{year}/combined_images')
    return good_years