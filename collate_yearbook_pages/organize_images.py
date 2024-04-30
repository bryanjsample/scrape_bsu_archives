import os
import shutil


def organize(src, year):
    dir_before = (sorted(os.listdir(src)))
    #if .DS_Store exists
    if '.DS_Store' in dir_before:
        #remove any .DS_Store files to enumerate properly
        os.remove(f'{src}/.DS_Store')
    #establish source directory
    ls_dir = (sorted(os.listdir(src)))
    print(len(ls_dir))
    #etablish directory to save some images
    saveDir = src.replace('/images', '')
    #iterate through files
    for item in ls_dir:
        test = item.upper()
        #rename front cover
        if test == 'FRONT_COVER.JPG' or test == 'COVER.JPG':
            os.rename(f'{src}/{item}', f'{src}/a_cover.jpg')
        #rename front end 1
        if test == 'FRONT_END_1.JPG' or test == 'FRONT_END1.JPG':
            os.rename(f'{src}/{item}', f'{src}/a_empty1.jpg')
        #rename front end 2
        if test == 'FRONT_END_2.JPG' or test == 'FRONT_END2.JPG':
            os.rename(f'{src}/{item}', f'{src}/a_empty2.jpg')
        #rename title page
        if test == 'TITLE_PAGE.JPG':
            os.rename(f'{src}/{item}', f'{src}/page_001')
        #rename back end 1
        if test == 'BACK_END_1.JPG' or test == 'BACK_END1.JPG':
            os.rename(f'{src}/{item}', f'{src}/z_empty1.jpg')
        #rename back end 2
        if test == 'BACK_END_2.JPG' or test == 'BACK_END2.JPG':
            os.rename(f'{src}/{item}', f'{src}/z_empty2.jpg')
        #rename front and back ends
        if test == 'FRONT_AND_BACK_ENDS.JPG' or test == 'BACK_AND_FRONT_ENDS':
            os.rename(f'{src}/{item}', f'{src}/a_empty1.jpg')
            shutil.copy(f'{src}/a_empty1.jpg', f'{src}/z_empty1.jpg')
        #rename front and back ends 1-4
        if test == 'FRONT_AND_BACK_ENDS_1-4.JPG':
            os.rename(f'{src}/{item}', f'{src}/a_empty1.jpg')
            shutil.copy(f'{src}/a_empty1.jpg', f'{src}/a_empty2.jpg')
            shutil.copy(f'{src}/a_empty1.jpg', f'{src}/z_empty1.jpg')
            shutil.copy(f'{src}/a_empty1.jpg', f'{src}/z_empty2.jpg')
        #rename front and back end 1
        if test == 'FRONT_AND_BACK_END1.JPG' or test == 'FRONT_AND_BACK ENDS1.JPG':
            os.rename(f'{src}/{item}', f'{src}/a_empty1.jpg')
            shutil.copy(f'{src}/a_empty1.jpg', f'{src}/z_empty1.jpg')
        #rename front and back end 2
        if (test) == 'FRONT_AND_BACK_END2.JPG' or test == 'FRONT_AND_BACK_ENDS2.JPG':
            os.rename(f'{src}/{item}', f'{src}/a_empty2.jpg')
            shutil.copy(f'{src}/a_empty2.jpg', f'{src}/z_empty2.jpg')
        #rename printer page
        if 'PRINTER' in test:
            os.remove(f'{src}/{item}')
        #rename back cover
        if test == 'BACK_COVER.JPG':
            os.rename(f'{src}/{item}', f'{src}/z_last.jpg')
        #move spine out of directory
        if test == 'SPINE.JPG':
            shutil.move(f'{src}/{item}', f'{saveDir}/{item}')
    #reestablish directory
    ls_dir = (sorted(os.listdir(src)))
    #adjust fortmat for these years

    #establish path to white jpeg 
    jpegPath = src.replace(f'/{year}/images', '/yearbooks')
    #adjust format for these years
    if year in [1951, 1958, 1959, 1960, 1961, 1962, 1965, 1971]:
        #add empty white pages in front and back
        shutil.copy(f'{jpegPath}/white.jpg', f'{src}/a_empty6')
        shutil.copy(f'{jpegPath}/white.jpg', f'{src}/z_empty01')
    #adjust format for 1971
    if year == 1971:
        #add empty white page in back only
        shutil.copy(f'{jpegPath}/white.jpg', f'{src}/z_empty01')
    #adjust format for these years
    if year in (1951, 1957, 1958, 1959, 1960, 1961, 1962, 1965, 1966, 1967, 1968, 1970, 1971):
        #move back cover out of directory so it doesn't get combined
        shutil.move(f'{src}/z_last.jpg', f'{saveDir}/z_last.jpg')
    #reesatablish directory
    ls_dir = (sorted(os.listdir(src)))
    #if theres an odd number of images
    if len(ls_dir) % 2 == 1.0:
        #move the cover page out of the directory
        shutil.move(f'{src}/a_cover.jpg', f'{saveDir}/a_cover.jpg')


    print("Images Organized")