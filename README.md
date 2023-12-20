# Download All Images From The Bemidji State University Archives

>The goal of this python script is to download every image that is not a yearbook from the [Bemidji State University Archives](midjistate.edu/library/archives/index.html).
>When executed, the script will make directories to organize each image that is downloaded.
>  - Each image is downlaoded in JPEG format.
>     - Some images are only available in TIFF format. The script will download them as JPEG images.
>  - Images are orgnized according to the webpage they were downloaded from.
>  - The images will be collated into a PDF file to quickly find an image.

### Inialization and Execution

---

1. **Form a directory in which you wish to save all images.**
2. **Open download_images.py**
   1. Edit line 12
      `src = ''`
      1. Paste the pile path of your target directory.
      2. Save the file.
3. **Execute the script.**

---

### Results

- Inside of your target directory, you will have multiple sub-directories containing all archived images.
- A PDF will be compiled of all images in each directory.
  - You can easy scroll through and find an image you would like to use.
---
