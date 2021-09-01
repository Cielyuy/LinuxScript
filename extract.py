import sys
import os
import shutil


def lm_find_files(path, targetType, targetDir, result=[]):
    """
    Basic Description:
            查找目录中指定类型的所有文件

    Detailed Description:

    Args:
        path: 查找的目录
		target: 目标文件类型，比如".json"
		result: 找到的目标文件列表
    Returns:
		result: 找到的目标文件列表
    Raises:
        exceptions
    """
    files = os.listdir(path);
    for f in files:
        npath = path + '\\' + f
        if (os.path.isfile(npath)):
            if (os.path.splitext(npath)[len(os.path.splitext(npath)) - 1] == targetType):
                result.append(npath)
                shutil.move(npath, targetDir+'\\'+f)

        if (os.path.isdir(npath)):
            if (f[0] == '.'):
                pass
            else:
                lm_find_files(npath, targetType, targetDir, result)
    return result


path1 = os.getcwd()
path = os.getcwd()
targetType = '.txt'
targetDir = path1 + '\\' + 'target\\'
if os.path.exists(targetDir):
    print('noDir')
else:
    os.mkdir(targetDir)
r1 = lm_find_files(path, targetType, targetDir, result=[])
for i in r1:
    print(i)
