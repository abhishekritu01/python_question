
string ='geeks quiz practice code'

# print(string[::-1]) #edoc ecitcarp ziuq skeeg

s = string.split()[::-1]
l=[]
print(s) #['code', 'practice', 'quiz', 'geeks']

for i in s:
    l.append(i[::-1])
print(" ".join(l))
