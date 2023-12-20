import cv2
import numpy as np
import os
import shutil

def combine(src, year):
    #initialize even counter at 000
    leftIter = '0'
    #initalize odd counter at 001
    rightIter = '1'
    #initialize combined counter at 000
    combinedIter = '0'
    #form a list containing iterators
    iters = [leftIter, rightIter, combinedIter]
    #form list of files in directory to iterate through
    album = sorted(os.listdir(src))
    #only iterate for half of the length of list
    numimages = range(int(len(album) / 2) + (int(len(album) % 2)))

    print(numimages, type(numimages))
    
    for images in numimages:
            #establish all variables formatted for combine
            leftValue = str(iters[0]).zfill(3)
            rightValue = str(iters[1]).zfill(3)
            combinedValue = str(iters[2]).zfill(3)
            #establish movepath
            movePath = src.replace('/images', '')

            #combine images
            #if even amount of images
            combiner(src, movePath, leftValue, rightValue, combinedValue)

            #iterate values
            counter(iters)
    #move the cover into combined folder
    move_cover(movePath)
    #prepare for new src in main
    # src = src.replace(f'/{year}/images', '')
    # return src

def combiner(src, movePath, leftValue, rightValue, combinedValue):
    #load the images
    leftImage = cv2.imread(f'{src}/rename_{leftValue}.jpg') 
    rightImage = cv2.imread(f'{src}/rename_{rightValue}.jpg')
    #resize the images
    leftImage = cv2.resize(leftImage, (1140, 1550))
    rightImage = cv2.resize(rightImage, (1140, 1550))
    #combine the images horizontally
    combinedImage = np.hstack((leftImage, rightImage))
    #display combined image (NOT NEEDED)
    # cv2.imshow('combined_image.jpg', combinedImage)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #save combined image
    cv2.imwrite(f'{movePath}/combined_images/combined_page_{combinedValue}.jpg', combinedImage)
    print(f'Combined page_{combinedValue}')

def counter(iters):
    #iterate left image to next even number
    leftIter = str(int(str(iters[0])) + 2)
    #iterate right image to next odd number
    rightIter = str(int(str(iters[1])) + 2)
    #iterate combined image to next number
    combinedIter = str(int(str(iters[2])) + 1)
    #return new values to main
    iters.clear()
    iters.extend([leftIter, rightIter, combinedIter])
    return(iters)

def move_cover(movePath):
    dir = os.listdir(movePath)
    if '.DS_Store' in dir:
     #remove any .DS_Store files to enumerate properly
        os.remove(f'{movePath}/.DS_Store')
    dir = os.listdir(movePath)
    #move files back into correct directory to be compiled into pdf
    if 'a_cover.jpg' in dir:
        shutil.move(f'{movePath}/a_cover.jpg', f'{movePath}/combined_images/a_cover.jpg')
    if 'Spine.jpg' in dir:
        shutil.move(f'{movePath}/Spine.jpg', f'{movePath}/combined_images/a_spine.jpg')
    if 'z_last.jpg' in dir:
        shutil.move(f'{movePath}/z_last.jpg', f'{movePath}/combined_images/z_last.jpg')
