import os

def create(src, yearbooks):
    lsDir = os.listdir(src)
    for year in yearbooks:
        #idempotent statement
        if str(year) in lsDir:
            print('Directories already exist.')
            exit()
        else:
            #for each year, create these dirs
            os.mkdir(f'{src}/{year}')
            os.mkdir(f'{src}/{year}/images')
            os.mkdir(f'{src}/{year}/combined_images')
