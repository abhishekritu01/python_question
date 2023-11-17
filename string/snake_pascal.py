
test ='hello_world'

def snake_to_pascal(string):
    l=string.split('_')
    print(l)
    l2=[]
    for i in l:
        l2.append(i.capitalize())
    return "".join(l2)

print(snake_to_pascal(test))
   


