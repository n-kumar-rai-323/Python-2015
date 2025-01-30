# sort
l1 = [(2,3), (1,1),(4,2),(5,5),(2,4)]



def function(data):
    return data[1]

l1.sort(key=function)
print(l1)