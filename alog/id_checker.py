import math
# 验证身份证号是否合规
# 校验码是否合法
def isValidCheckCode(cardNO):
    ws=[]
    nums=[]
    s=0
    for i in range(len(cardNO)):
        if(cardNO[i].upper()=='X'):
            nums.append(10)
        else:
            nums.append(int(cardNO[i]))
        ws.append(math.pow(2,17-i)%11)
        s+=nums[i]*ws[i]
    lastnum=s%11
    return lastnum==1

# 产生所有的指定前缀的身份证号
def generateCards(prefix):
    result=[prefix]
    tmplist=[]
    for i in range(4):
        for cardno in result:
            for j in ['0','2']:
                tmplist.append(cardno+j)
        result=tmplist.copy()
        tmplist.clear()
    return result

if __name__=='__main__':
    # 产生所有只有2和0 组成的身份证号
    card_nos=generateCards('22020220200202')
    result=[]
    for card_no in card_nos:
        if(isValidCheckCode(card_no)):
            result.append(card_no)
    print('有效的身份证号是:',result)
    

