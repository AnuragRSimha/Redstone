from platform import *
import extract_windows
import extract_linux
from sys import *
os = system()
f = open("design.txt", "r")
print(f.read())
f.close()
if(os=="Windows"):
    print("Redstone detected Windows OS. Starting extraction on windows...")
    extract_windows.extract(argv[1],argv[2])
else:
    print("Redstone detected Linux OS. Starting extraction on Linux...")
    extract_linux.extract(argv[1])