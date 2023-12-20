import requests
from bs4 import BeautifulSoup
import os
import img2pdf
import urllib.request

#TEST

def main():
    #USER INPUT
    #INITIALIZE SOURCE WHERE ALL IMAGES WILL BE SAVED
    src = '/Users/bryansample/vscode/alumni/images'

    #set url to BSU archives
    url = 'https://www.bemidjistate.edu/library/archives/index.html'

    #USER INPUT
    #IF YOU WISH TO RUN ONLY ONE PAGE, INSERT '/examplepage.html' INTO mainIndex_hrefs BRACKETS AND COMMENT LINES 26 - 31.
    #initialize empty global
    mainIndex_hrefs = []

    #if .DS_Store exists
    if '.DS_Store' in os.listdir(src):
        #remove any .DS_Store files to enumerate properly
        os.remove(f'{src}/.DS_Store')
    #idempotent statement
    if len(os.listdir(src)) > 0:
        print('Ensure that your source directory is empty.')
        exit()

    #get hrefs from main index
    get_main_hrefs(url, mainIndex_hrefs)

    #filter out yearbooks
    mainIndex_hrefs = [subIndex for subIndex in mainIndex_hrefs if 'Ah-Mic' not in subIndex]
    mainIndex_hrefs = [subIndex for subIndex in mainIndex_hrefs if 'AH-MIC' not in subIndex]
    mainIndex_hrefs = [subIndex for subIndex in mainIndex_hrefs if 'Beaver' not in subIndex]

    #IF ONLY OBTAINING ONE PAGE
    #iterate throught the main index, navigating to each sub index
    for subIndex in mainIndex_hrefs:
        #remove old webpage from url path
        url = url.replace('index.html', '')
        dirPath = subIndex.replace('/index.html', '')
        #confirmation print
        print(f'Starting {subIndex}')

        #make required directories for specific url
        make_dirs(src, dirPath)

        #replace new webpage into url path
        subUrl = url + subIndex
        #initialize lists
        subIndex_hrefs = []
        imgUrls = []
        tifUrls = []
        #clear out any potential items in lists
        subIndex_hrefs.clear()
        imgUrls.clear()
        tifUrls.clear()

        #obtain hrefs from sub index
        get_sub_hrefs(subUrl, subIndex_hrefs)

        #navigate to image container webpage
        get_img_url(subUrl, subIndex_hrefs, imgUrls, tifUrls)

        #save images into their target directory
        save_img(subUrl, imgUrls, tifUrls, src, dirPath)

        #adjust images to all be jpg format
        tiff_to_jpeg(src, dirPath)

        #compile pdf from images
        compile_pdf(src, dirPath)

        #confirmation print
        print(f'Finished with {subIndex}')

def get_main_hrefs(url, mainIndex_hrefs):
    #obtain html parse
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    #set target div to form a list from
    targetDiv = soup.find('div', id = 'imagepanel')
    #form the list
    mainIndex_a = targetDiv.find_all('a')
    #iterate through list, finding href and appending it to href list
    for href in mainIndex_a:
        path = href.get('href')
        mainIndex_hrefs.append(path)
    
def make_dirs(src, dirPath):
    #split dirPath into individual elements to name the directories
    dirs = dirPath.split('/')
    #establish variables for directory names

    if len(dirs) == 1:
        #establish variable for directory names
        dir1 = dirs[0].lower()
        if dir1 not in os.listdir(src):
            os.mkdir(f'{src}/{dir1}')

    elif len(dirs) == 2:
        #establish variables for directory names
        dir1 = dirs[0].lower()
        dir2 = dirs[1].lower()
        #make dir 1 if it doesnt exist
        if dir1 not in os.listdir(src):
            os.mkdir(f'{src}/{dir1}')
        #make dir 2 if it doesnt exist
        if dir2 not in os.listdir(f'{src}/{dir1}'):
            os.mkdir(f'{src}/{dir1}/{dir2}')

    elif len(dirs) == 3:
        #establish variables for directory names
        dir1 = dirs[0].lower()
        dir2 = dirs[1].lower()
        dir3 = dirs[2].lower()
        #make dir 1 if it doesnt exist
        if dir1 not in os.listdir(src):
            os.mkdir(f'{src}/{dir1}')
        #make dir 2 if it doesnt exist
        if dir2 not in os.listdir(f'{src}/{dir1}'):
            os.mkdir(f'{src}/{dir1}/{dir2}')
        #make dir 3 if it doesnt exist
        if dir3 not in os.listdir(f'{src}/{dir1}/{dir2}'):
            os.mkdir(f'{src}/{dir1}/{dir2}/{dir3}')
    elif len(dirs) == 4:
        #establish variables for directory names
        dir1 = dirs[0].lower()
        dir2 = dirs[1].lower()
        dir3 = dirs[2].lower()
        dir4 = dirs[3].lower()
        #make dir 1 if it doesnt exist
        if dir1 not in os.listdir(src):
            os.mkdir(f'{src}/{dir1}')
        #make dir 2 if it doesnt exist
        if dir2 not in os.listdir(f'{src}/{dir1}'):
            os.mkdir(f'{src}/{dir1}/{dir2}')
        #make dir 3 if it doesnt exist
        if dir3 not in os.listdir(f'{src}/{dir1}/{dir2}'):
            os.mkdir(f'{src}/{dir1}/{dir2}/{dir3}')
        #make dir 4 if it doesnt exist
        if dir4 not in os.listdir(f'{src}/{dir1}/{dir2}/{dir3}'):
            os.mkdir(f'{src}/{dir1}/{dir2}/{dir3}/{dir4}')
    else:
        print('Something went wrong. Check your URL.')
        exit()

def get_sub_hrefs(subUrl, subIndex_hrefs):
    #obtain html parse
    req = requests.get(subUrl)
    soup = BeautifulSoup(req.content, 'html.parser')
    #set target div to form a list from
    targetDiv = soup.find('div', id = 'imagepanel')
    #form the list
    subIndex_a = targetDiv.find_all('a')
    #iterate through list, finding href and appending it to href list
    for href in subIndex_a:
        path = href.get('href')
        subIndex_hrefs.append(path)
    
def get_img_url(subUrl, subIndex_hrefs, imgUrls, tifUrls):
    #iterate through sub index to navigate to image container webpages
    for page in subIndex_hrefs:
        #remove old webpage from sub url path
        subUrl = subUrl.replace('index.html', '')
        #replace new webpage into sub url path
        imgUrl = subUrl + page
        req = requests.get(imgUrl)
        soup = BeautifulSoup(req.content, 'html.parser')
        targetImg = soup.find('img')
        if targetImg is None:
            tifDiv = soup.find('div', id = 'tiffimagepanel')
            tif_a = tifDiv.find('a')
            tif_href = tif_a.get('href')
            tifUrls.append(tif_href)
        else:
            imgUrls.append(targetImg['src'])
            # print(f'Obtained {targetImg['src']}')

def save_img(subUrl, imgUrls, tifUrls, src, dirPath):
    #download jpegs
    for page in imgUrls:
        #remove old webpage from sub url path
        subUrl = subUrl.replace('index.html', '')
        #replace new webpage into sub url path
        imgUrl = subUrl + page
        imgName = page.lower()
        #requests, extracts, and stores data in targetpage
        imgData = requests.get(imgUrl).content
        file = open(f'{src}/{dirPath}/{imgName}', 'wb')
        file.write(imgData)
        file.close()
    #download tifs
    for tifPage in tifUrls:
        #remove old webpage from sub url path
        subUrl = subUrl.replace('index.html', '')
        #replace new webpage into sub url path
        tifUrl = subUrl + tifPage
        tifName = tifPage.lower()
        #obtain image from url
        urllib.request.urlretrieve(tifUrl, f'{src}/{dirPath}/{tifName}')
    
def tiff_to_jpeg(src, dirPath):
    for item in os.listdir(f'{src}/{dirPath}'):
        if '.tiff' in item:
            name = item.strip('.tiff')
            os.rename(f'{src}/{dirPath}/{item}', f'{src}/{dirPath}/{name}.jpg')
        elif '.tif' in item:
            name = item.strip('.tif')
            os.rename(f'{src}/{dirPath}/{item}', f'{src}/{dirPath}/{name}.jpg')

def compile_pdf(src, dirPath):
    #change cwd to directory containing images
    os.chdir(f'{src}/{dirPath}')
    #compile pdf from images in cwd
    with open('compiled_images.pdf', 'wb') as pdf:
        pdf.write(img2pdf.convert([i for i in sorted(os.listdir(os.getcwd())) if i.endswith('.jpg')]))
    print(f'Compiled pdf in {src}/{dirPath}')


main()
