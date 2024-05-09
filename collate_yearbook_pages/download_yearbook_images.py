'''
    download_yearbook_images.py
    Author : Bryan Sample

    Module to scrape and download images from yearbooks off of the BSU Archives webpage.
'''

from bs4 import BeautifulSoup
from typing import List
from time import sleep
import requests
import os


def download(source_path:str, year:int) -> None:
    '''
        Make sure that source directory is empty (other than DS_Store) then obtain and save each image into the directory.
        Arguments:
            - source_path : string | path to parent directory where sub-dirs will be made and images will be saved
            - year : integer  | current year in the iteration
    '''
    url = f'https://www.bemidjistate.edu/library/archives/Ah-Mic_{year}/'
    if len(os.listdir(source_path)) > 1:
        print(f'Something went wrong and there are already items in {source_path}')
        exit()
    else:
        href_ls = get_links(url)
        url_ls = get_img_url(url, href_ls)
        save_img(source_path, url, url_ls)


def get_links(url:str) -> List[str]:
    '''
        Scrape the index.html page of the targeted year to obtain the links for each page, add them to a list, then return the list.
        Arguments:
            - url : string | url of the target year
    '''
    href_ls:List[str] = []
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
    return href_ls

def get_img_url(url:str, href_ls:List[str]) -> List[str]:
    '''
        Scrape the img src element in the page for each href, add it to a list, then return the list.
        Arguments:
            - url : string | url of the target year
            - href_ls : list of strings | list containing href links pointing to each indvidual page
    '''
    url_ls = []
    #iterate objects in href list to navigate to each webpage
    for loc in href_ls:
        #establish soup variables based on current page
        req = requests.get(url + loc)
        sleep(.5)
        soup = BeautifulSoup(req.content, 'html.parser')
        #find image on page
        target = soup.find('img')
        #add image source to url list
        url_ls.append(target['src'])
        print(f'Obtained {target['src']}')
    return url_ls

def save_img(source_path:str, url:str, url_ls:List[str]) -> None:
    '''
        Scrape the image data for each img src element and save each of them into the source path.
        Arguments:
            - source_path : string | path to parent directory where sub-dirs will be made and images will be saved
            - url : string | url of the target year
            - url_ls : list of strings | list containing href links pointing to each indvidual image source
    '''
    #iterate objects in url list to navigate to each webpage
    for img in url_ls:
        #establishes what image url we want to go to
        targetPage = url + img
        #requests, extracts, and stores data in targetpage
        imgData = requests.get(targetPage).content
        sleep(.5)
        #opens file with image name in savepath to store data
        with open(f'{source_path}/{img}', 'wb') as f:
            #saves the data
            f.write(imgData)
        print(f'Saved {img}')
