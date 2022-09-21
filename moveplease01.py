#!/usr/bin/env python3
"""Script to move files """

# import standard library
import shutil # this will be used to move files
import os # this will provide access to low level os operation

def main():
    # start in the home user directory
    os.chdir('/home/student/mycode/')

    # move the file or folder
    shutil.move('raynor.obj', 'ceph_storage/')

    # pause and ask for new file name
    xname = input('What is the new name for kerrigan.obj? ')
    # rename the current file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


main()
