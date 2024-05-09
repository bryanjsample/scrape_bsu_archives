'''
    module.py
    Author : Bryan Sample

    Module to combine images into a user-friendly collated view and merge the images into a PDF file.
'''

import cv2
import numpy as np
import os
import shutil
from typing import List
from PIL import Image

def combine(src_path:str):
    '''
        Combine images to created a collated view.
        Arguments:
            - src_path : string | path to parent directory where sub-dirs will be made and images will be saved
    '''
    #form a list containing counters for left page, right page, and combined page numbers.
    page_counters = ['0', '1', '0']
    #form list of files in directory to iterate through
    album = sorted(os.listdir(src_path))
    #only iterate for half of the length of list
    num_combined_images = range(len(album) // 2 + len(album) % 2)
    
    for image in num_combined_images:
            #establish all variables formatted for combine
            page_counters = [f'{x:0>3}' for x in page_counters]
            print(page_counters)
            #establish movepath
            dest_path = src_path.replace('/images', '')
            combiner(src_path, dest_path, page_counters)
            page_counters = counter(page_counters)
    move_cover(dest_path)

def combiner(src_path:str, dest_path:str, page_counters:List[str]):
    '''
        This function does the actual combining.
        Arguments:
            - src_path : string | path to parent directory where sub-dirs will be made and images will be saved
            - dest_path : string | path to year directory
            - page_counters : list of strings | contains z-filled integer strings to keep track of which page will be placed on the left, right, and also tracks the combined page number
    '''
    #load the images
    leftImage = cv2.imread(f'{src_path}/rename_{page_counters[0]}.jpg') 
    rightImage = cv2.imread(f'{src_path}/rename_{page_counters[1]}.jpg')
    #resize the images
    leftImage = cv2.resize(leftImage, (1140, 1550))
    rightImage = cv2.resize(rightImage, (1140, 1550))
    #combine the images horizontally
    combinedImage = np.hstack((leftImage, rightImage))
    cv2.imwrite(f'{dest_path}/combined_images/combined_page_{page_counters[2]}.jpg', combinedImage)
    print(f'Combined page_{page_counters[2]}')

def counter(page_counters:List[str]) -> List[str]:
    '''
        Adjust the counter to make sure that file names are correct.
        Arguments:
            - page_counters : list of strings | contains z-filled integer strings to keep track of which page will be placed on the left, right, and also tracks the combined page number
    '''
    #iterate left image to next even number
    page_counters[0] = f'{int(page_counters[0])+2:0>3}'
    #iterate right image to next odd number
    page_counters[1] = f'{int(page_counters[1])+2:0>3}'
    #iterate combined image to next number
    page_counters[2] = f'{int(page_counters[2])+1:0>3}'
    return page_counters

def move_cover(dest_path:str):
    '''
        Move covers back into the directory after the pages have been combined.
        Arguments:
            - dest_path : string | path to year directory
    '''
    dir = os.listdir(dest_path)
    if '.DS_Store' in dir:
    #remove any .DS_Store files to enumerate properly
        os.remove(f'{dest_path}/.DS_Store')
    dir = os.listdir(dest_path)
    #move files back into correct directory to be compiled into pdf
    if 'a_cover.jpg' in dir:
        shutil.move(f'{dest_path}/a_cover.jpg', f'{dest_path}/combined_images/a_cover.jpg')
    if 'Spine.jpg' in dir:
        shutil.move(f'{dest_path}/Spine.jpg', f'{dest_path}/combined_images/a_spine.jpg')
    if 'z_last.jpg' in dir:
        shutil.move(f'{dest_path}/z_last.jpg', f'{dest_path}/combined_images/z_last.jpg')

def create_pdf_from_images(src_path:str, year:int) -> None:
    '''
        Create a pdf containing all of the combined images.
        Arguments:
            - src_path : string | path to parent directory where sub-dirs will be made and images will be saved
            - year : integer | current year in the iteration
    '''
    pdf_path = src_path.replace('/images', '')
    pages = [Image.open(f'{pdf_path}/combined_images/{x}') for x in sorted(os.listdir(f'{pdf_path}/combined_images')) if '.jpg' in x]
    pages[0].save(f'{pdf_path}/{year}_yearbook.pdf', 'PDF', resolution=100.0, save_all=True, append_images=pages[1:])


