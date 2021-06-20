import random as r
ss = '1234567890.,/qwertyuiop[]\'asdfghjkl;zxcvbnm./'

for y in range(10):
    str1 = ''
    for x in range(10):
        str1 += ss[r.randint(0, len(ss)-1)]
    print(str1)