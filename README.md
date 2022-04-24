![logo](https://user-images.githubusercontent.com/53004679/164986375-b32a9b45-059e-4c1a-8ff7-bec604a16b93.png)

# Execution

## I. For Linux

### A. Disk image files (.img)
1. Guarantee that you have installed Python.
2. Consider a sample disk file named NTFS.img

To extract it's contents, type:
``` python3 redstone.py NTFS.img``` 
or, 
```python redstone.py NTFS.img```

### B. Encase image files (.E01)
1. Run the program as mentioned previously.
2. When you are promoted for an input, a space delimitered sequence is accepted. 
Format: file_system offset

a) The first argument is the file system of a partition in the image file (Select a single partition). This is noted by looking into the "Description" from the table displayed before you. 

b) The second argument, being an offset value, only a number is accepted.  This is noted from the "Start" column of the desired partition. Enter only those digits succeeding the consecutive zeros.

## II. For Windows
(Encase files are not yet supported)
1. Install 7-Zip from https://7-zip.org/download.html
(Important: Remember the path you provide during the installation.)
2. Decide the destination to store all the contents of your disk image.
3. Copy the path to the source file (img file).
4. Run the program: 
```python3 redstone.py "path\to\img_file" "path\to\the\destination"```
Replace path\to\img_file and path\to\the\destination accordingly.
5. You would be prompted to provide the path to the directory of 7-Zip. Enter the path that you had noted in step 1 of this process.
