import shutil
import os

dir = os.listdir("E:/PYTHON__/DUMMY")

for a in dir:
    root , ext = os.path.splitext("E:/PYTHON__/DUMMY/"+a)
    if os.path.exists("E:/PYTHON__/DUMMY/"+ext) :
        shutil.move("E:/PYTHON__/DUMMY/"+a , "E:/PYTHON__/DUMMY/"+ext)
    elif (os.path.exists("E:/PYTHON__/DUMMY/"+ext) == False):
        os.mkdir("E:/PYTHON__/DUMMY/"+ext)
        shutil.move("E:/PYTHON__/DUMMY/"+a , "E:/PYTHON__/DUMMY/"+ext)




