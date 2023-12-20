import make_dirs
import download_images
import organize_images
import rename_images
import combine_images

def main():
    # #ALL YEARS
    # #obtain all years
    # yearbooks = list(range(1957, 1972))

    #SELECT YEARS
    #obtain select years ([year1, year2, year3, year4, etc...])
    yearbooks = [1951]

    #ESTABLISH DIRECTORY IN WHICH ALL IMAGES WILL BE SAVED
    #ENSURE THAT 'YEARBOOKS' DIRECTORY IS CONTAINED WITHIN THIS DIRECTORY
    #ENSURE THAT THERE ARE NO OTHER ITEMS IN DIRECTORY BESIDES 'YEARBOOKS' DIRECTORY
    src = '/Users/bryansample/vscode/alumni'

    #form directories for year
    make_dirs.create(src, yearbooks)

    #iterate through yearbooks
    for year in yearbooks:
        print(f'STARTING {year}')
        #reestablishes source directory for years other than the first
        if year != int(yearbooks[0]):
            lastYear = year - 1
            newSrc = src.replace(f'{lastYear}/images', '')
            #reestablish source directory
            src = f'{newSrc}/{year}/images'
        else:
            #reestablish source directory for the first year in the list
            src = f'{src}/{year}/images'

        #run function to download images
        download_images.download(src, year)

        #run function to organize images
        organize_images.organize(src, year)
        
        #run function to rename files
        rename_images.rename(src)

        #combine all images in directory
        combine_images.combine(src, year)

        #compile pdf

        #end main
main()

