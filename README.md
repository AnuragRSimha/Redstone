![logo](https://user-images.githubusercontent.com/53004679/164986375-b32a9b45-059e-4c1a-8ff7-bec604a16b93.png)

# Introduction
### Image Evidences & Digital Forensics
Cybercrime has become an inexorable threat nowadays. With the advancement of technology, cybercriminals employ vivid techniques to triumph their satanic goals. To thwart these (cyber) ruffians, cyber investigators come into play. A cyber police/investigator obtains a piece of evidence, technically termed a _disk image_, that can be burnt onto any disk attached to the detective's PC. A couple of popular disk image extensions are .IMG, .ISO and .E01. 

### About Redstone
Redstone is a tool that functions to a similar degree as FTK imager or Autopsy of The Sleuth Kit (TSK) does. A detective can supply an evidence file (disk image) to the tool and provide Redstone with a couple of seconds to extract all the contents of it into a folder. It's rudimentarily a disk image extractor which aids the investigator in digging deeper into the case. With files of enormous size, Redstone could stretch for a while to complete the extraction into a directory.

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
(Encase files are not supported)
1. Install 7-Zip from https://7-zip.org/download.html
(Important: Remember the path you provide during the installation.)
2. Decide the destination to store all the contents of your disk image.
3. Copy the path to the source file (img file).
4. Run the command as below, replacing the image file and destination (folder) name: 
```python3 redstone.py NTFS.img extracted```
5. You would be prompted to provide the path to the directory of 7-Zip. Enter the path that you had noted in step 1 of this process.

# Additional Information
1. Developed in Karnataka, South India.
2. Programmed in python.

# Notice
Redstone is currently designed to function on not any other OS but Windows and Linux.
