import sys
import os
import shutil


def lm_find_files(path, targetType, targetDir, result=[]):
    """
    Basic Description:
            \u67e5\u627e\u76ee\u5f55\u4e2d\u6307\u5b9a\u7c7b\u578b\u7684\u6240\u6709\u6587\u4ef6

    Detailed Description:

    Args:
        path: \u67e5\u627e\u7684\u76ee\u5f55
		target: \u76ee\u6807\u6587\u4ef6\u7c7b\u578b\uff0c\u6bd4\u5982".json"
		result: \u627e\u5230\u7684\u76ee\u6807\u6587\u4ef6\u5217\u8868
    Returns:
		result: \u627e\u5230\u7684\u76ee\u6807\u6587\u4ef6\u5217\u8868
    Raises:
        exceptions
    """
    files = os.listdir(path);
    for f in files:
        npath = path + '/' + f
        if (os.path.isfile(npath)):
            if (os.path.splitext(npath)[len(os.path.splitext(npath)) - 1] == targetType):
                result.append(npath)
                #lensplitext = len(os.path.splitext(npath)
                #print(lensplitext)

                #npatha = (os.path.splitext(npath))[0,lensplitext]#.replace('-2800','-1800')
                #print(npatha)
                #os.rename(npath,npatha)
                shutil.move(npath, targetDir+'/'+f)

        if (os.path.isdir(npath)):
            if (f[0] == '.'):
                pass
            else:
                lm_find_files(npath, targetType, targetDir, result)
    return result


path1 = os.getcwd()
path = os.getcwd()
targetType = '.h5'
targetDir = path1 + '/' + 'target1/'
if os.path.exists(targetDir):
    print('noDir')
else:
    os.makedirs(targetDir)

r1 = lm_find_files(path, targetType, targetDir, result=[])

for i in r1:
    print(i)
