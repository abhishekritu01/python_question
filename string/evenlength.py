
string = 'geeks quiz aa practice code'

s = string.split()

for i in s:
    if len(i) % 2 == 0:
        print(i,'even')
    else:
        print(i,'odd')