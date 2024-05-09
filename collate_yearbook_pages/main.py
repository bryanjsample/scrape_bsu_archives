'''
    main.py
    Author : Bryan Sample

    Python script to scrape, download, organize, collate, and merge images into a PDF file to create a user-friendly view of yearbooks from the Bemidji
    State University Archives.

    External Dependencies:
        - cv2 || pip install opencv-python
        - bs4 || pip install bs4
        - requests || pip install requests
        - pillow || pip install pillow
'''

from typing import List
import os
import make_dirs
import download_yearbook_images
import combine_yearbook_images
import organize_images

def scrape_yearbooks(target_years:None|List[int]=None, src_path:None|str=None) -> None:
    '''
        Scrape, download, organize, collate, and merge images into a PDF for target years' yearbooks in the BSU Archives.
        Arguments:
            - target_years : None or a list of valid integers | if none... all years will be downloaded
            - src_path : None or a string | path to parent directory where sub-dirs will be made and images will be saved if none... directory structure will be built in the current working directory of the python shell
    '''
    if target_years is None:
        years = list(range(1957, 1972))
    elif type(target_years) is list:
        years = years
    else:
        print('Something is wrong with your targeted years. Check your arguments.')
    if src_path is None:
        src_path = os.getcwd()

    # form directory to store images and create subdirectories for each year
    os.mkdir(f'{src_path}/examples')
    src_path += '/examples'
    years = make_dirs.create_directories(src_path, years)

    for year in years:
        print(f'\n\nSTARTING {year}')
        #reestablishes source directory based on current year
        if year == years[0]:
            src_path = f'{src_path}/{year}/images'
        else:
            last_year = year - 1
            src_path = src_path.replace(f'{last_year}/images', f'{year}/images')

        download_yearbook_images.download(src_path, year)
        organize_images.organize(src_path, year)
        organize_images.rename(src_path)
        combine_yearbook_images.combine(src_path)
        combine_yearbook_images.create_pdf_from_images(src_path, year)
        print(f'\nPDF compiled for {year}.')

def main():
    scrape_yearbooks(src_path='/Users/bryanjsample/Documents/code/github/scrape_bsu_archives/collate_yearbook_pages')

if __name__ == '__main__':
    main()

