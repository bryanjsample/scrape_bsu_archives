'''
    organize_images
    Author : Bryan Sample

    Organizes directory of yearbooks photos to ensure proper formatting when combined.

    ** Originally written as my very first large python script...I am sorry for this mess of an if block
'''

import os
import shutil

def organize(src_path:str, year:str):
    '''
        Organize images to ensure proper formatting when collating.
        Arguments:
            src_path : string | path to parent directory where sub-dirs will be made and images will be saved
            year : integer | year of the images
    '''
    dir_before = (sorted(os.listdir(src_path)))
    #if .DS_Store exists
    if '.DS_Store' in dir_before:
        #remove any .DS_Store files to enumerate properly
        os.remove(f'{src_path}/.DS_Store')
    #establish source directory
    ls_dir = (sorted(os.listdir(src_path)))
    #etablish directory to save some images
    dest_dir_path = src_path.replace('/images', '')
    #iterate through files
    for item in ls_dir:
        test = item.upper()
        #rename front cover
        if test == 'FRONT_COVER.JPG' or test == 'COVER.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/a_cover.jpg')
        #rename front end 1
        if test == 'FRONT_END_1.JPG' or test == 'FRONT_END1.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/a_empty1.jpg')
        #rename front end 2
        if test == 'FRONT_END_2.JPG' or test == 'FRONT_END2.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/a_empty2.jpg')
        #rename title page
        if test == 'TITLE_PAGE.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/page_001')
        #rename back end 1
        if test == 'BACK_END_1.JPG' or test == 'BACK_END1.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/z_empty1.jpg')
        #rename back end 2
        if test == 'BACK_END_2.JPG' or test == 'BACK_END2.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/z_empty2.jpg')
        #rename front and back ends
        if test == 'FRONT_AND_BACK_ENDS.JPG' or test == 'BACK_AND_FRONT_ENDS':
            os.rename(f'{src_path}/{item}', f'{src_path}/a_empty1.jpg')
            shutil.copy(f'{src_path}/a_empty1.jpg', f'{src_path}/z_empty1.jpg')
        #rename front and back ends 1-4
        if test == 'FRONT_AND_BACK_ENDS_1-4.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/a_empty1.jpg')
            shutil.copy(f'{src_path}/a_empty1.jpg', f'{src_path}/a_empty2.jpg')
            shutil.copy(f'{src_path}/a_empty1.jpg', f'{src_path}/z_empty1.jpg')
            shutil.copy(f'{src_path}/a_empty1.jpg', f'{src_path}/z_empty2.jpg')
        #rename front and back end 1
        if test == 'FRONT_AND_BACK_END1.JPG' or test == 'FRONT_AND_BACK ENDS1.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/a_empty1.jpg')
            shutil.copy(f'{src_path}/a_empty1.jpg', f'{src_path}/z_empty1.jpg')
        #rename front and back end 2
        if (test) == 'FRONT_AND_BACK_END2.JPG' or test == 'FRONT_AND_BACK_ENDS2.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/a_empty2.jpg')
            shutil.copy(f'{src_path}/a_empty2.jpg', f'{src_path}/z_empty2.jpg')
        #rename printer page
        if 'PRINTER' in test:
            os.remove(f'{src_path}/{item}')
        #rename back cover
        if test == 'BACK_COVER.JPG':
            os.rename(f'{src_path}/{item}', f'{src_path}/z_last.jpg')
        #move spine out of directory
        if test == 'SPINE.JPG':
            shutil.move(f'{src_path}/{item}', f'{dest_dir_path}/{item}')
    #reestablish directory
    ls_dir = (sorted(os.listdir(src_path)))
    #adjust fortmat for these years

    #establish path to white jpeg 
    jpegPath = src_path.replace(f'/examples/{year}/images', '')
    #adjust format for these years
    if year in [1951, 1958, 1959, 1960, 1961, 1962, 1965, 1971]:
        #add empty white pages in front and back
        shutil.copy(f'{jpegPath}/white.jpg', f'{src_path}/a_empty6')
        shutil.copy(f'{jpegPath}/white.jpg', f'{src_path}/z_empty01')
    #adjust format for 1971
    if year == 1971:
        #add empty white page in back only
        shutil.copy(f'{jpegPath}/white.jpg', f'{src_path}/z_empty01')
    #adjust format for these years
    if year in (1951, 1957, 1958, 1959, 1960, 1961, 1962, 1965, 1966, 1967, 1968, 1970, 1971):
        #move back cover out of directory so it doesn't get combined
        shutil.move(f'{src_path}/z_last.jpg', f'{dest_dir_path}/z_last.jpg')
    #reesatablish directory
    ls_dir = (sorted(os.listdir(src_path)))
    #if theres an odd number of images
    if len(ls_dir) % 2 == 1.0:
        #move the cover page out of the directory
        shutil.move(f'{src_path}/a_cover.jpg', f'{dest_dir_path}/a_cover.jpg')


    print("Images Organized")


def rename(src_path:str):
    '''
        Rename images to ensure proper formatting when collating.
        Arguments:
            src_path : string | path to parent directory where sub-dirs will be made and images will be saved
    '''
    parent_dir = (sorted(os.listdir(src_path)))
    for count, filename in enumerate(parent_dir):
        #sets new name of file according to the enumerated count, filled up to 3 characters with zeroes
        newname = f'rename_{str(count).zfill(3)}.jpg'
        old = f'{src_path}/{filename}'
        new = f'{src_path}/{newname}'
        print(f'Renamed {count}')
        os.rename(old, new)