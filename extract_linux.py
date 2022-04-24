import subprocess as sp
import os
from sys import argv

def extract(src):
    print("Redstone has initiated the extraction of "+src+" on Linux OS.")
    # Required functions
    def create_directory():
        print("\nCreating the directory(s) to mount "+src)
        os.system("mkdir /mnt")
        os.system("mkdir /mnt/sdb")
        os.system("mkdir /mnt/windows_mount")
        print("Done")

    # Get the present working directory
    cmd = "pwd"
    pwd = sp.getoutput(cmd)

    # Extraction of encase file
    if(".E01" in src):
        print("Installing/Configuring ewf-tools...\n")
        os.system("apt install ewf-tools")

        # Create the mounting directory
        if(os.path.exists("/mnt/sdb") == True):
            try:
                os.system("umount /mnt/sdb")
                os.system("umount /mnt/windows_mount")

            finally:
                os.system("rm -r /mnt")
                create_directory()
        else:
            create_directory()

        # ewfmount mounts encase files
        os.system("ewfmount "+src+" /mnt/sdb")
        os.system("mmls /mnt/sdb/ewf1")

        # Start the extraction
        while(True):
            try:
                print("\nType 'quit' to exit")
                fs_offset = input("\nFrom the table displayed above, enter the file system (look into the description) and the starting offset (Format: file_system offset): ")
                
                if('quit' in fs_offset):
                    break
                
                fs_offset = fs_offset.split()
                os.system("umount /mnt/windows_mount")
                
                if(fs_offset[0].upper() == 'NTFS'):
                    os.system("mount -t ntfs -o loop,ro,show_sys_files,stream_interface=windows,offset=$(({}*512)) /mnt/sdb/ewf1 /mnt/windows_mount/".format(fs_offset[1]))
                else:
                    os.system("mount -o loop,offset=$(({}*512)) /mnt/sdb/ewf1 /mnt/windows_mount/".format(fs_offset[1]))
                
                print("The contents in the root directory are:")
                print(sp.getoutput("ls /mnt/windows_mount"))
                
                if(os.path.exists("/"+pwd+"/windows_mount") == True):
                    os.system("rm -r /"+pwd+"/windows_mount")
                
                os.system("cp -r /mnt/windows_mount "+pwd)
                print("\nSaved the contents to "+pwd+"/windows_mount")
            
            except:
                print("\nThe input was invalid.")
        
        # Unmount and delete
        os.system("umount /mnt/sdb")
        os.system("umount /mnt/windows_mount")
        os.system("rm -r /mnt")
        exit(0)

    # Create mount directory
    if(os.path.exists("/mnt/sdb") == True):
        try:
            os.system("umount /mnt/sdb")
        finally:
            os.system("rm -r /mnt")
        create_directory()
    else:
        create_directory()

    # Start mounting
    os.system("mount -o loop "+src+" /mnt/sdb")

    # Get the contents
    cmd = "ls -r /mnt/sdb"
    ls = sp.getoutput(cmd)
    if(ls == "/mnt/sdb:"):
        print("A fatal error occurred while mounting the disk image. Exiting the program...")
        exit(1)
    else:
        print("\nContents in the root directory of "+src+" are:")
        print(ls)

    # Copy the contents
    if(os.path.exists("/"+pwd+"/sdb") == True):
        os.system("rm -r /"+pwd+"/sdb")
    os.system("cp -r /mnt/sdb "+pwd)
    print("\nSaved the contents to "+pwd+"/sdb")

    # Unmount
    os.system("umount /mnt/sdb")
    os.system("rm -r /mnt")
    print("\nUnmounted the image file and removed the directory.")
