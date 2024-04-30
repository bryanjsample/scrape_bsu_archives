from bs4 import BeautifulSoup
import requests
import os


def download(src, year):
    url = f'https://www.bemidjistate.edu/library/archives/Ah-Mic_{year}/'
    href_ls = []
    url_ls = []
    #idempotent statement (1 accounts for .DS_Store file if it exists)
    if len(os.listdir(src)) > 1:
        print('There are already photos saved into the directory.')
        exit()
    else:
        get_links(url, href_ls)
        get_img_url(url, href_ls, url_ls)
        save_img(url, url_ls, src)


def get_links(url,href_ls):
    #set variables for BeautifulSoup based on url
    req = requests.get(url + 'index.html')
    soup = BeautifulSoup(req.content, 'html.parser')
    #sets the div id to target for extraction
    targetDiv = soup.find('div', id = 'imagepanel')
    #forms list of all a components
    a_list = targetDiv.find_all('a')
    #print <a> vertically FOR CONFIRMATION
    for href in a_list:
        link = href.get('href')
        href_ls.append(link)

def get_img_url(url, href_ls, url_ls):
    #iterate objects in href list to navigate to each webpage
    for loc in href_ls:
        #establish soup variables based on current page
        req = requests.get(url + loc)
        soup = BeautifulSoup(req.content, 'html.parser')
        #find image on page
        target = soup.find('img')
        #add image source to url list
        url_ls.append(target['src'])
        print(f'Obtained {target['src']}')

def save_img(url, url_ls, src):
    #iterate objects in url list to navigate to each webpage
    for img in url_ls:
        #establishes what image url we want to go to
        targetPage = url + img
        #requests, extracts, and stores data in targetpage
        imgData = requests.get(targetPage).content
        #opens file with image name in savepath to store data
        file = open(f'{src}/{img}', 'wb')
        #saves the data
        file.write(imgData)
        #closes the file
        file.close()
        print(f'Saved {img}')
