import os
import os.path as op
import random
import string
import shutil

def get_target_dir(name):
    mapping = {
            ('exe', 'msi'):'Apps',
            ('txt', 'pdf', 'docs', 'xlsx'):'Docs',
            ('zip', 'rar', '7z'):'Archives',
            ('avi', 'mp4'):'Vedios',
            ('mp3'):'Musics',
            ('png', 'gif', 'jpg'):'Pictures',
    }
    ext = name.split('.')[-1]
    for exts,target_dir in mapping.items():
        if ext in exts:
            return target_dir
    return 'Unknown'

def organize_file(download_dir):
    os.chdir(download_dir)  # change to directory
    names = os.listdir()    # list all thing in current dir.

    for name in names:
        if op.isfile(name):
            #获取目标文件夹
            target_dir = get_target_dir(name)
            if not op.isdir(target_dir):
                os.mkdir(target_dir)
            #检查目标文件
            target_name = op.join(target_dir, name)
            if op.isfile(target_name):
                print("File exists, skip", target_name)
            else:
                #移动文件
                shutil.move(name, target_name)

    # show files tree
    cmd = 'tree /f ' + download_dir
    os.system(cmd)


if __name__ == '__main__':
    download_dir = input("Input download dir path:")
    organize_file(download_dir)
