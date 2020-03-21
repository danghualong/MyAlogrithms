#encoding=utf-8
import re
'''
"将中缀运算式转化为后缀运算符（能去掉括号）
然后计算结果"
例如：
中缀运算式：a*(b+c)-d/e+f
后缀运算式abc+*de/-f+
'''
p={
    "#":[0,0],
    ")":[1,10],
    "+":[2,2],
    "-":[2,2],
    "*":[3,3],
    "/":[3,3],
    "(":[10,1]
    }

#是否是数值
def isdigit(str):
    p= re.compile("[0-9]+\.?[0-9]*")
    if p.match(str):
        return True
    else:
        return False
#括号是否有效
def isValid(exp):
    bs=[]
    for i in exp:
        if i=="(":
            bs.append(i)
        elif i==")":
            if(len(bs)<=0):
                return False
            bs.pop()
    return len(bs)==0
#将中缀转化为后缀
def transform(exp):
    result=[]
    opds=[]
    opds.append("#")
    for i in exp:
       if isdigit(i):
           result.append(i)
       else:
           #空栈直接存入
           if(len(opds)==0):
               opds.append(i)
           #当栈内优先级小于待入栈优先级
           elif p[opds[len(opds)-1]][1]<p[i][0]:
               opds.append(i)
           else:
               while(len(opds)>0):
                   semiPoped=opds[len(opds)-1]
                   #如果遇到右括号，则最近的左括号之间的所有出栈
                   if(i==")"):
                       if semiPoped!="(":
                           result.append(semiPoped)
                           opds.pop()
                       else:
                            opds.pop()
                            break
                   else:
                       if(p[semiPoped][1]>=p[i][0]):
                           result.append(semiPoped)
                           opds.pop()
                       else:
                           opds.append(i)
                           break
    #剩余操作符出栈(第一个#例外）
    while len(opds)>1:
        result.append(opds.pop())
    return result
#根据后缀计算结果
def calculate(exp):
    opds=[]
    for i in exp:
        if isdigit(i):
            opds.append(float(i))
        else:
            right=opds.pop()
            left=opds.pop()
            if i== "+":
                left+=right
            elif i=="-":
                left-=right
            elif i=="*":
                left*=right
            elif i=="/":
                if right==0:
                    raise Exception("don't divided by 0")
                left/=right
            opds.append(left)
    return opds.pop()
#格式化输出
def formatPrint(exp,sep=''):
    str=''
    tmp=''
    for i in exp:
        str+=(tmp+i)
        tmp=sep
    return str

if __name__=="__main__":
    exp=['6','*','(','3','+','5',')','-','2','/','4','+','10']
    str1=formatPrint(exp)
    print(str1)
    isvalid=isValid(exp)
    if isvalid:
        result=transform(exp) 
        print(formatPrint(result,sep=' ')) 
        str1=str1+"="+str("%.1f" %calculate(result))
        print(str1)            
