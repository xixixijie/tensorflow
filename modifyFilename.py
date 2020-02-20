import os
#设定文件路径
path='/home/aiyunji/cxj/models/research/deeplab/datasets/lv/mask'

#对目录下的文件进行遍历
for file in os.listdir(path):
#判断是否是文件
    if os.path.isfile(os.path.join(path,file))==True:
#设置新文件名
        print(file)
        new_name=file.replace("_json_label","")
        print(new_name)
# #重命名
        os.rename(os.path.join(path,file),os.path.join(path,new_name))
# #
#结束
print ("End")
