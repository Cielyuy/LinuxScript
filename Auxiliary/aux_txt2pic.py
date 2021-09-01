import re,os,shutil

def SplitStr(nameList):
    # re_fuhao =  re.compile(r'\_(\-?[0-9]+)$')##匹配字符串的末尾数字
    re_fuhao =  re.compile(r'\_(\-?[0-9]+)\.txt')##匹配字符串的末尾数字
    return int((re_fuhao.findall(nameList))[0])
    

# b = SplitStr('cir_1_5000')
# print(type(b))
# import sys
# print(sys.path)
# l1 = [cirP1,cirP2,cirP3,line_1,line_2]
# l2 = ['line_2','cirP1','line_1','cirP2','A']
# print(l2.sort())

##对提取的字符串进行排序
def ListOrder(listPre):
    return sorted(listPre,key = lambda keys:[ord(i) for i in keys],reverse=False)

# print(ListOrder(l2))

###
###将其中的带有双引号的地址，替换成绝对地址
def turn2AbsPath(line,absPathClipDir,houZhuiNum):

    re_txtStoredWhole = re.compile(r'\"\S*txt\"') 
    re_txtStored = re.compile(r'\"(\S+)\.txt\"')
    
    a_Whole = re_txtStoredWhole.findall(line)
    a = re_txtStored.findall(line)
    if a_Whole != []:
        a1 = a[0]+'_'+houZhuiNum+'.txt'
        c = os.path.join(absPathClipDir,a1)
        line = line.replace(a_Whole[0],c)
        return line
    else:
        return line


# d = r'/solve/monitors/surface/set-monitor cirPoint1  "Sum" velocity-magnitude cirPoint1 () n n y "miao_V_huan_4.txt" 100'
# p = turn2AbsPath(d,'C','3')
# print(p)