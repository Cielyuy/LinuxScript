import shutil, os, sys

def devideSqueue(num, list=[]):
    # list_Div[][]= None
    # i = 0
    shang = len(list) // num
    yu = len(list) % num
    list_Div = []

    # for i in range(num):
    #     list_Div.append([])

    if len(list) <= num:
        for i in range(len(list)):
            list_Div.append(list[i])

        print('single squeu')
        # return list_Div
    else:
        # shang = len(list) // (num - 1)
        # yu = len(list) % (num - 1)
        k = -1
        for i in range(0, len(list)):
            if yu == 0:
                if i % shang == 0:
                    list_Div.append([])
                    k = k + 1
                    # list_Div.append([])
                    list_Div[k].append(list[i])
                else:
                    list_Div[k].append(list[i])

            elif k < yu & yu != 0:
                if i % (shang + 1) == 0:
                    list_Div.append([])
                    k = k + 1
                    # list_Div.append([])
                    list_Div[k].append(list[i])
                else:
                    list_Div[k].append(list[i])


            elif ((i - yu * (shang + 1)) % shang) == 0:
                list_Div.append([])
                k = k + 1
                list_Div[k].append(list[i])
            else:
                list_Div[k].append(list[i])


    return list_Div

def listGet(a, b, c):
    numList = list()
    if (b - a) % c == 0:
        d = (b - a) / c
        i = 0
        while i <= d:
            numList.append(a + i * c)
            i = i + 1

    else:
        d = (b - a) / c
        i = 0
        while i <= d:
            numList.append(a + i * c)
            i = i + 1

        numList.append(b)

    return numList



# 前缀命名
#ExtendClip = False

VelocityOrPressure = False              ########################################首先要进行判断

FirstPara = 4000  ##################################

LastPara = 5000  ##################################

CountNum = 100

Mesh_num_preffix = 'M500_'

varNum = 85

absoluteDir = os.getcwd() + "/"  #############         地址命名    ###############
Clip_Whole_Dir = os.path.abspath(os.path.dirname(os.getcwd())) + "/"

Mesh_load_dir_preffix = 'basic_Mesh' + '/'
MeshName = 'Model_500.msh'
Mesh_Load_Dir = Clip_Whole_Dir + Mesh_load_dir_preffix + MeshName

catchList = listGet(FirstPara, LastPara, CountNum)

for j in catchList:
    print(j)

totalDivideList = devideSqueue(12,catchList)
total_Clip_Number = len(totalDivideList)

for count_Total_Clip_Number in range(0,total_Clip_Number):
#Every_Clip_Number =
#Specified_Dir = "0712" + '/'  ###############指定储存复制文件的特定文佳夹
    Specified_Dir_preffix_1 = "0713_testOneDimention"
    Specified_Dir_preffix_2 = '/p2800' + '_'
    Specified_Dir = Specified_Dir_preffix_1  + Specified_Dir_preffix_2 + str(count_Total_Clip_Number)+'/'
    if os.path.exists(Clip_Whole_Dir+Specified_Dir):
        print('good')
    else:
        os.makedirs(Clip_Whole_Dir+Specified_Dir)


    Stored_Example_J_Name = 'Example_J.jou'
    Stored_Example_J_middle_dir = 'basic_Mesh' + '/'
    Stored_Example_J_Dir = Clip_Whole_Dir + Stored_Example_J_middle_dir + Stored_Example_J_Name

    Stored_Example_C_Name = 'Example_C.cse'
    Stored_Example_C_middle_dir = 'basic_Mesh' + '/'
    Stored_Example_C_Dir = Clip_Whole_Dir + Stored_Example_C_middle_dir + Stored_Example_C_Name

    B_J_middle_name_preffix = 'J_' + Mesh_num_preffix + str(varNum) + '_'
    B_C_middle_name_preffix = 'C_' + Mesh_num_preffix + str(varNum) + '_'

    B_J_Content_Preffix = 'call fluent 3ddp -t32 -g -wait -i '
    B_C_Content_Preffix = "call cfdpost -batch "

    # bat文件 和 cse文件
    B_J_Name = 'BF_' + Mesh_num_preffix + str(FirstPara) + "_" + str(varNum) + ".bat"
    B_J_Dir = Clip_Whole_Dir + Specified_Dir + B_J_Name
    B_C_Name = 'BP_' + Mesh_num_preffix + str(FirstPara) + "_" + str(varNum) + ".bat"
    B_C_Dir = Clip_Whole_Dir + Specified_Dir + B_C_Name

    # 清除原先有的bat文件
    print(os.getcwd())
    # for files in os.listdir(os.getcwd()):
    for files in os.listdir(Clip_Whole_Dir + Specified_Dir):
        if files.endswith(".bat"):
            os.remove(os.path.join(Clip_Whole_Dir + Specified_Dir, files))

    linuxShName = 'linuxDocu.sh'
    linux_content_preffix_1 = 'fluent  -g  3d  -t16 -wait -cnf=$hostlist   -mpi=intel -i '

    #shutil.copyfile(src,trg)
    shutil.copyfile(Clip_Whole_Dir + Stored_Example_J_middle_dir + linuxShName,Clip_Whole_Dir + Specified_Dir + 'B_' +linuxShName)
    # linuxSh = open(Clip_Whole_Dir + Stored_Example_J_middle_dir + linuxShName, "a+", encoding="utf-8")

    # 命名更改 复制
    k = totalDivideList[count_Total_Clip_Number]
    B_J_Middle_Name = B_J_middle_name_preffix + str(k) + ".jou"
    B_J_Exported_Dir = Clip_Whole_Dir + Specified_Dir + B_J_Middle_Name  #####################命名jou等中间文件名称
    B_C_Middle_Name = B_C_middle_name_preffix + str(k) + ".cse"
    B_C_Exported_Dir = Clip_Whole_Dir + Specified_Dir + B_C_Middle_Name

    c_src = Stored_Example_C_Dir  # 原文件信息
    c_trg = B_C_Exported_Dir  # 现文件信息

    j_src = Stored_Example_J_Dir  # 原文件信息
    j_trg = B_J_Exported_Dir  # 现文件信息

    b_linux_sh = open(Clip_Whole_Dir + Specified_Dir +'B_' + linuxShName, "a+", encoding="utf-8")
    b_j_f = open(B_J_Dir, 'a+', encoding="utf-8")
    b_c_f = open(B_C_Dir, 'a+', encoding="utf-8")

    # sh bat case文件编写
    B_linux_Docu = linux_content_preffix_1 + B_J_Middle_Name + '\n'
    B_J_Docu = B_J_Content_Preffix + j_trg + "\n"
    B_C_Docu = B_C_Content_Preffix + c_trg + "\n"
    b_linux_sh.write(B_linux_Docu)
    b_j_f.write(B_J_Docu)
    b_c_f.write(B_C_Docu)

    #########第一个文件替换功能
    f_c = open(c_src, "r", encoding="utf-8")
    # j_trg = absoluteDir+fileDis+str(k)+'_1'+".txt"
    f_c_new = open(c_trg, "a+", encoding="utf-8")

    # FluentDataName = 'FluentData_' + str(Mesh_num_preffix) + str(k) + "_" + str(varNum)
    # cfdpostDataName = "CP_" + str(Mesh_num_preffix) + str(k) + '_' + str(varNum)
    #
    # C_find_str_ls = ["P_317_80_1800.jpg", 'R_317_80_1800.dat']  ##################更换匹配字符
    # C_replace_str_ls = [cfdpostDataName + ".jpg", FluentDataName + '.dat']  #################
    #########################################################################
    #############################################################################
    FluentDataName = 'FluentData_' + str(Mesh_num_preffix) + str(k) + "_" + str(varNum)
    cfdpostDataName = "CP_" + str(Mesh_num_preffix) + str(k) + '_' + str(varNum)

    C_Previous_Stored_Dat = "D:\\ZTC\\0707\\V85\\FluentData_M317__-20_85.dat"
    C_Now_Dat = Clip_Whole_Dir + Specified_Dir + FluentDataName + '.dat'
    C_Previous_Stored_Pic = "D:\\ZTC\\0707\\V85\\CP_M317__-20_85.jpg"
    C_Now_Pic = Clip_Whole_Dir + Specified_Dir + cfdpostDataName + ".jpg"

    C_find_str_ls = [C_Previous_Stored_Pic, C_Previous_Stored_Dat]  ##################更换匹配字符
    C_replace_str_ls = [C_Now_Pic, C_Now_Dat]  #################

    J_Previous_Stored_Mesh = "/file/read-case Me_317.msh"
    J_Now_mesh = '/file/read-case ' + Mesh_Load_Dir
    J_Previous_Stored_Cas = 'FluentData_M317__52_1800.cas'
    J_Now_Cas = Clip_Whole_Dir + Specified_Dir + FluentDataName + '.cas'
    J_Previous_Stored_Pic = 'FluentData_M317__52_1800jpg'
    J_Now_Pic = Clip_Whole_Dir + Specified_Dir + FluentDataName + 'jpg'

    J_Previous_Velocity = 'velocity-inlet i1  n n y y n 52'
    J_Now_Velocity = 'velocity-inlet i1  n n y y n ' + str(k)
    J_Now_Velocity_varNum = 'velocity-inlet i1  n n y y n ' + str(varNum)

    J_Previous_Pressure = 'pressure-outlet o1  y n -1800'
    J_Now_Pressurue = 'pressure-outlet o1  y n ' + str(k)
    J_Now_Pressurue_varNum = 'pressure-outlet o1  y n ' + str(varNum)
    if VelocityOrPressure:
        J_Previous_Var = J_Previous_Velocity
        J_Now_Var = J_Now_Velocity
        J_Previous_varNum = J_Previous_Pressure
        J_Now_varNum = J_Now_Pressurue_varNum
    else:
        J_Previous_Var = J_Previous_Pressure
        J_Now_Var = J_Now_Pressurue
        J_Previous_varNum = J_Previous_Velocity
        J_Now_varNum = J_Now_Velocity_varNum

    J_find_str_ls = [J_Previous_Stored_Mesh, J_Previous_Stored_Cas, J_Previous_Stored_Pic,
                     J_Previous_Var，J_Previous_varNum]  ##################更换匹配字符
    J_replace_str_ls = [J_Now_mesh, J_Now_Cas, J_Now_Pic, J_Now_Var, J_Now_varNum]  ##################

    #########################################################################
    ###########################################################################

    for line in f_c:
        # print(line)
        m = 0
        # print(len(find_str_ls))
        while m < len(C_find_str_ls):
            line = line.replace(C_find_str_ls[m], C_replace_str_ls[m])
            m = m + 1
            # print(line)

        # print(line)
        f_c_new.write(line)
        # f_new.flush
        # print(f_new)
    f_c.close()
    f_c_new.close()
    b_j_f.close()
    b_c_f.close()
    b_linux_sh.close()

    #####第二个文件替换功能
    f_j = open(j_src, "r", encoding="utf-8")
    # j_trg = absoluteDir+fileDis+str(k)+'_1'+".txt"
    f_j_new = open(j_trg, "a+", encoding="utf-8")

    ##########FluentDataName = 'FluentData_'+str(c)+'_'+str(k)+"_"+str(d)

    # J_find_str_ls = ["R_317_85_1800.cas", 'R_317_85_1800.jpg', 'n n y y n 85']  ##################更换匹配字符
    # J_replace_str_ls = [FluentDataName + '.cas', FluentDataName + 'jpg', 'n n y y n ' + str(k)]  ##################

    for line in f_j:
        # print(line)
        m = 0
        # print(len(J_find_str_ls))
        while m < len(J_find_str_ls):
            line = line.replace(J_find_str_ls[m], J_replace_str_ls[m])
            m = m + 1
            # print(line)

        # print(line)
        f_j_new.write(line)
        # f_new.flush
        # print(f_new)
    f_j.close()
    f_j_new.close()

    print("shashasha???")

    b_j_f = open(B_J_Dir, 'r', encoding="utf-8")
    b_c_f = open(B_C_Dir, 'r', encoding="utf-8")
    # 合并执行文档
    comFile = open(Clip_Whole_Dir + Specified_Dir + "B_comFile.bat", "a+", encoding="utf-8")

    print("shashasha!!!")

    for line in b_j_f:
        print("111111" + line)
        comFile.write(line)

    for line in b_c_f:
        print("222" + line)
        comFile.write(line)

    b_j_f.close()
    b_c_f.close()
    comFile.close()
