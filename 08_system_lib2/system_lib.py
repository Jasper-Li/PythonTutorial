# 08 system module, lib

import datetime

now = datetime.datetime.now()
print('now  is', now)
print('date is', now.date())
print('time is', now.time())
print()

import os           #import system library/module
def print_dir_info():
    cwd = os.getcwd()
    print('Current working dir', cwd)
    files = os.listdir()
    print('Files:', files)
    print('Count:', len(files))
    print()
    return cwd

cwd = print_dir_info()
os.chdir('c:')
print_dir_info()
