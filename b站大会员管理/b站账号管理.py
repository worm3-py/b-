import datetime
import random as r
def initialization():
    a=datetime.date.today()
    print(a)
    with open('date.txt','r') as f1:
        date=(f1.read())
        if date=='':
            date=input('请输入到期时间：')
            list1=date.split(',')
            list2=[]
            for x in list1:
                list2.append(int(x))
            #date=(list2[0],list2[1],list2[2])
            #print(date)
            date=datetime.date(list2[0],list2[1],list2[2])
            with open('date.txt', 'w') as f2:
                f2.write(str(date))
        else:

            list1 = date.split('-')
            list2 = []
            for x in list1:
                #print(x)
                list2.append(int(x))
            date=datetime.date(list2[0],list2[1],list2[2])

    print('距到期还有'+str(date-a))
initialization()
def add(id,data):
    with open('users.txt','r') as f1:
        users=eval(f1.read())
        a = datetime.date.today()
        b = a+datetime.timedelta(days=data)
        users[id]=[a,b]
    with open('users.txt','w') as f2:
        f2.write(str(users))
    print('添加成功')
def delete(id):

    with open('users.txt','r') as f1:
        users=eval(f1.read())
    a=users[id]
    #del users[id]
    e= users.pop(id,'404')
    if e == '404':
        print(None)
    else :
        with open(id+'.txt','a+') as f2:
            print(a)
            f2.write('\n'+str(a))
        with open('users.txt','w') as f3:
            f3.write(str(users))
    print('删除成功')
    ss = '1234567890.,/qwertyuiop[]\'asdfghjkl;zxcvbnm./'
    str1 = ''
    for x in range(10):
        str1 += ss[r.randint(0, len(ss)-1)]

    with open('new key.txt','a+') as f1:
        f1.write('\n'+str(datetime.date.today())+' '+str1)
        print('新密码:' + str1)

def find(id):
    with open('users.txt','r') as f1:
        users=eval(f1.read())
    print(users[id])
def watch():
    with open('users.txt','r') as f1:
        users=eval(f1.read())
    for x in users:
        print(x,users[x])
def look():
    with open('users.txt', 'r') as f1:
        users = eval(f1.read())
    for x in users:
        a=datetime.date.today()
        b=users[x][1]
        a=str(b-a)
        #print(a)
        list1=a.split(' ')
        if int(list1[0]) <= 0:
            print(x,users[x],list1[0],'过期')
        else:
            print(x,users[x],list1[0])
def renew(id,date):
    with open('users.txt', 'r') as f1:
        users = eval(f1.read())
    user=users[id]
    user[1]+=datetime.timedelta(days=date)
    users[id]=user
    with open('users.txt','w') as f2:
        f2.write(str(users))
    print('续期成功')
while True:
    try:
        a=input('>>')
        if 'add' in a:
            list1=a.split(' ')
            add(list1[1],int(list1[2]))
        elif a=='watch':
            watch()
        elif 'del' in a:
            list1 = a.split(' ')
            delete(list1[1])
        elif 'find' in a:
            list1 = a.split(' ')
            find(list1[1])
        elif a=='break':
            break
        elif a=='look':
            look()
        elif 'renew' in a:
            list1 = a.split(' ')
            renew(list1[1],int(list1[2]))

    except:
        print('错误')




'''
直冲
365天120元
30天20元
540天160元
共号
365天60
150天30
30天8元
7天3元
1天1元



可以点赞评论
不能投币
不能发布违规信息
不能投稿
不准私自使用b币，卡卷
不得外借
'''