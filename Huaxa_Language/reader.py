var_dict={}
#var_dict.update({'b':'fuck'})
def printColor(col,idl,end='\n'):print("\033[0;%dm%s\033[0m"%(col,idl),end=end)
def printColorE(col,idl):print("\033[0;%dm%s\033[0m,"%(col,idl),end='')
def inputColor(col,idl):return input("\033[0;%dm%s\033[0m"%(col,idl))
黑=30;红=31;绿=32;黄=33;蓝=34;紫=35;青=36;白=37
var_list=list(var_dict.items())
# print(var_list)
def fenjie(commandline):
    a=[]
    for i in commandline:a.append(i)
    return a
def getvarname(list):
    global var_list
    a=[]
    for i in var_list:a.append(i[0])
    return a
def getvarvalue(list):
    global var_list
    a=[]
    for i in var_list:a.append(i[1])
    return a
def 判断(Code_List,i):
    global var_list
    if not '本行注释: '==Code_List[:6]:
        if '输出('==Code_List[i][:3] and ')'==Code_List[i][-1]:
            cmdl=fenjie(Code_List[i])
            var_list=list(var_dict.items())
            if '<' in Code_List[i] and '>' in Code_List[i]:
                if getvarname(var_list).count(Code_List[i][cmdl.index('<')+1:cmdl.index('>')])>0:
                    for ii in range(1,Code_List[i].count('<')+1):
                        vvl=getvarvalue(var_list)
                        vnl=getvarname(var_list)
                        print(vvl[vnl.index(Code_List[i][cmdl.index('<')+1:cmdl.index('>')],ii)])
                else:
                    if ',结尾:[{' in Code_List[i][3:-1]:
                        print(Code_List[i][3:-1-7-abs(cmdl.index('}')-cmdl.index('{'))],end=Code_List[i][cmdl.index('{')+1:cmdl.index('}')])
                    else:
                        print(Code_List[i][3:-1])
            elif ',结尾:[{' in Code_List[i][3:-1]:
                print(Code_List[i][3:-1-7-abs(cmdl.index('}')-cmdl.index('{'))],end=Code_List[i][cmdl.index('{')+1:cmdl.index('}')])
            else:
                print(Code_List[i][3:-1])
        if '数字型变量('==Code_List[i][:6] and ')'==Code_List[i][-1]:
            #<变量名>
            cmdl=fenjie(Code_List[i])
            value=Code_List[i][6:-1].split(',')
            value[1]=float(value[1])
            var_list=list(var_dict.items())
            var_dict.update({value[0]:value[1]})
            #print(list(var_dict.items()))
        if '字符型变量('==Code_List[i][:6] and ')'==Code_List[i][-1]:
            #~变量名~
            value=Code_List[i][6:-1].split(',')
            var_list=list(var_dict.items())
            var_dict.update({value[0]:value[1]})
            #print(var_dict)
    var_list=list(var_dict.items())
def reader(Code_List):
    for i in range(len(Code_List)):
        判断(Code_List,i)
reader(['数字型变量(var,1)','数字型变量(var1,2)','输出(<var><a>)'])
# reader(['输出(1,结尾:[{ 23}])','输出(1)','输出(a)','数字型变量(var,1.1223)','数字型变量(var,12)','字符型变量(var3,d)','输出(a)'])
# var_list=list(var_dict.items())
# print(var_list)
