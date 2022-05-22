'''
modules from other directories
'''
import sys

print(sys.path)

'''
MacOS:
nano ~/.bash_profile

OR

export PYTHONPATH='file_path'
'''

file_1 = open('test.jpg', 'rb')

with open('pic_copy.jpg', 'wb') as wf:
    all = file_1.read()
    wf.write(all)