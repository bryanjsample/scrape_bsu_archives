import os


def rename(src):
    #establish parent directory as sorted list (INCLUDING ANY .DS_STORE)
    
    #re-establish parent directory as sorted list (EXCLUDING .DS_STORE)
    parent_after = (sorted(os.listdir(src)))
    #enumerate each file in dir and set variables for rename
    for count, filename in enumerate(parent_after):
        #sets new name of file according to the enumerated count, filled up to 3 characters with zeroes
        newname = f'rename_{str(count).zfill(3)}.jpg'
        #filepath of old
        old = f'{src}/{filename}'
        #filepath of new
        new = f'{src}/{newname}'
        #confirmation print
        print(f'Renamed {count}')
        #rename
        os.rename(old, new)

