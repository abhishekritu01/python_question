
def search_element(arr,element):
    for i in arr:
        if i == element:
            return True 
    return False

arr = [1,2,3,4,5]
element = 3

print(search_element(arr,element))