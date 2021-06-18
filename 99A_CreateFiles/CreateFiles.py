import os
import sys
import os.path as op
import random
import string

def create_random_file(size, ext):
    for i in range(size):
        body = ''.join(random.choices(string.ascii_letters +string.digits, k=6))
        if len(ext) > 0:
            filename = body + '.' + ext
        else:
            filename = body
        open(filename, 'a').close()
        print(filename)


def create_files(download_dir):
    if not op.isdir(download_dir):
        os.mkdir(download_dir)
    os.chdir(download_dir)
    exts = [
        'exe', 'msi',
        'txt', 'pdf', 'docs', 'xlsx',
        'zip', 'rar', '7z',
        'avi', 'mp4',
        'mp3',
    ]
    count = 0
    count_no_ext = 4
    for ext in exts:
        size_list = random.choices(range(1,4))
        size = size_list[0]
        create_random_file(size, ext)
        count = count + size 
    create_random_file(count_no_ext, '')
    count += count_no_ext
    print("Create {} files".format(count))

if __name__ == '__main__':
    download_dir = input("Input download dir path:")
    create_files(download_dir)
    sys.exit(0)
