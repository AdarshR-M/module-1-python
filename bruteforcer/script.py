# Flag is flag{b1n42y_s3r2ch_f7w}

import os
import subprocess as sub

# os.system('wget -O bruteforcer https://github.com/CSecIITB/module-1-python/blob/main/bruteforcer/bruteforcer?raw=true') 

# os.system('wget -O wordlist.txt https://github.com/CSecIITB/module-1-python/blob/main/bruteforcer/wordlist.txt?raw=true')

a = os.getcwd()
# os.system('chmod +x bruteforcer')
# os.system('rm bruteforcer')
# os.system('rm wordlist.txt')

def state(s):
    b = sub.check_output(['printf '+s+' | ./bruteforcer'], shell = True)
    c = b.decode('utf-8')
    d = c[22:27] != 'WRONG'
    if d:
        return 0
    elif c[-4] == 'l' and not d:
        return -1
    elif c[-5] == 'h' and not d:
        return 1

f = open('wordlist.txt', 'r')

Ans = ''
h = 'z'
l = '0'
n = 0
while True:
    n += 1
    if n%10000 == 0:
        print(n, Ans)
    s = f.readline()
    if not s:
        break
    s = s[0:-1]
    if s > l and s < h:
        if state(s) == 0:
            Ans = s
            break
        elif state(s) == -1:
            l = s
        elif state(s) == 1:
            h = s
print('HERE')
fl = sub.check_output(['printf '+Ans+' | ./bruteforcer'], shell = True)
flag = fl.decode('utf-8')

print(flag)
