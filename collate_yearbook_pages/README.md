# Download and Collate Yearbooks from Bemidji State University Archives.

>#### When executed, this script will:
>1. Make directories for each yearbook on the [Bemidji State University Archives](https://www.bemidjistate.edu/library/archives/index.html)
>2. Iterate through each yearbook:
    a. Download all images from the yearbook index.
    b. Organize all of the images to be collated.
    c. Rename each image to ensure proper formatting.
    d. Collate two images at a time to create a left and right page.

---

### Initialization and Execution
1. Create a directory in which all files will be saved.
2. Open all_years.py
   - To download all years at once:
        1. Ensure that line 14 is commented and will not be executed.
        2. Ensure that line 10 is not commented.
        3. Edit line 19:
            `src = ''`
           1. Paste the path to your target directory inside of the single quotes.
        4. Save all_years.py
   - To download only one year at a time:
       1. Ensure that line 10 is commented and will not be executed.
       2. Ensure that line 14 is not commented.
       3. Edit line 19:
            `src = ''`
           1. Paste the path to your target directory inside of the single quotes.
        4. Save all_years.py
3.  Execute all_years.py

---

#### Result

1. Inside of your target directory you will have sub-directories containing:
   1. All individual JPEG images
   2. All collated images that you can then compile into a pdf.

>The images are named to be organized alphabetically in a file viewer.
>Once compiled, you will have an entire digital yearbook.