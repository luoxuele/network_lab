import os
import shutil


# def findAllFile(base):
#     for root,dirs,files in os.walk(base):
#         # for f in fs:
#         #     # yield f
#         #     print(f)
#         print(root)
#         print(dirs)
#         print(files)
#         print("-------------")



# findAllFile('.')

# os.rmdir("./h3cne/stp/ConfigDisk")
# os.removedirs("./h3cne/stp/SerialFile")
# shutil.rmtree("./h3cne/stp/.git")
# os.remove("./h3cne/stp/.gitignore")

# print(os.listdir("."))
# for i in os.listdir("."):
#     print(i,os.path.isdir(i),os.path.abspath(i))


# os.path.abspath


# 遍历目录
def traverse_dir(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # print(item,"-----------------")
            if (item == ".git") | (item == "ConfigDisk") | (item == "SerialFile"):
                print("delete dir:", item_path)
                shutil.rmtree(item_path)
                continue
            traverse_dir(item_path)
        else:
            if item == '.gitignore':
                print("delete file:", item_path)
                os.remove(item_path)
                continue
            


traverse_dir(".")