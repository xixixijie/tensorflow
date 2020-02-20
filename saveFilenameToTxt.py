import sys

import os


def ListFilesToTxt(dir, file, wildcard, recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)

        if (os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname, file, wildcard, recursion)
        else:
            print(name[0:-4])
            file.write(name[0:-4]+"\n")
            # for ext in exts:
            #     if (name.endswith(ext)):
            #         file.write(name + "\n")
            #         break


def Test():
    #dir放的是image的路径
    dir = "models/research/deeplab/datasets/lv/image"
    #out放的是train.txt的路径，可以改成val.txt等，不过我都是从train.txt复制一部分进val.txt的，可以写程序改成随机分配。
    outfile = "models/research/deeplab/datasets/lv/index/train.txt"
    
    wildcard = ".txt .exe .dll .lib"

    file = open(outfile, "w")
    if not file:
        print("cannot open the file %s for writing" % outfile)

    ListFilesToTxt(dir, file, wildcard, 0)

    file.close()


Test()

sys.exit()
