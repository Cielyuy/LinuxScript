import re , os,sys
sys.path.append(r'C:\Users\TRY-7220\Anaconda3\Lib')
sys.path.append(r'C:\Users\TRY-7220\Anaconda3\Library')
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib
sys.path.append(r'E:\LGF\Sim\Script\Auxiliary')
from aux_txt2pic import *
# DirList1 = [x for x in o]
clipDir1 = os.getcwd()
clipDir = clipDir1
print(clipDir)
#字母
re_ZiMu = re.compile(r'[a-z]+')
re_XiaoShu = re.compile(r'\d+\.?\d*')


txtDirListAll = [x for x in os.listdir('.') if '.txt' in x]

##特定几何特征的数据获取
spcifiedObj = 'cirPoint1'
pointCir1_List = ListOrder([x for x in txtDirListAll if spcifiedObj in x])
# print(pointCir1List)
df = pd.DataFrame()
listVam = []
listValue = []
for i in pointCir1_List:
    print(i)
    l0 = []
    l0.append(SplitStr(i))
    l1 = []
    d1 = os.path.join(clipDir,i)
    with open(d1,'r',encoding='utf-8') as docu :
        for line in docu.readlines():
            if re_ZiMu.findall(line) == []:
                # l0.append(SplitStr(i))
                l1.append((re_XiaoShu.findall(line))[1])
                # isFlag = False
            else:
                pass
        listVam.append(l0[0])
        endValue = l1[len(l1)-1]
        listValue.append(endValue)
        
        # df[i.split(".")[0]] = l1
df['pressure'] = listVam
df['velocity'] = listValue
excelName = spcifiedObj +'.xlsx'
excelDir = os.path.join(clipDir,excelName)
df.to_excel(excelDir,index = False)

plt.figure(spcifiedObj)
plt.title(spcifiedObj)
df[df.columns[1]] = df[df.columns[1]].apply(lambda x:round(float(x),2))##保留两位小数
plt.plot(df[df.columns[0]],df[df.columns[1]])

plt.xlabel('perssure')
plt.ylabel("value")

plt.savefig(spcifiedObj+'.png')
print('Done!')