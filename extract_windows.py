import subprocess as sp
import os
from sys import argv

def start(src, dst, dir_7zip, slash_last):
    print("Redstone has initiated the extraction of "+slash_last+" on Windows OS.")
    os.chdir(dir_7zip)
    if(os.path.exists(src)):
        os.system("7z x  \"{}\" -y -o\"{}\"".format(src,dst))
        print("\nThe contents in the root directory of your input file are:")
        for i in os.listdir(dst):
            print(i)
    else:
        print("Fatal error: File is inexistent.")
def extract(src, dst):
    slash_last = src.split('\\')[::-1]
    cwd = os.getcwd()
    dir_7zip = input("Enter the path to 7-Zip directory: ")
    if (len(slash_last)==1):
        slash_last = src
        start(cwd+'\\'+src, cwd+'\\'+dst, dir_7zip, slash_last)
    else:
        slash_last = slash_last[-1]
        start(src, dst, dir_7zip, slash_last)
