# sort
l1 = [(2,3), (1,1),(4,2),(5,5),(2,4)]



def function(data):
    return data[1]

l1.sort(key=function)
print(l1)




# task
a = [(4,12,5), (6,1), (11,12),(6,7,8)]

def lastIndex(data):
    return data[-1]
a.sort(key=lastIndex)
print(a)


a=["hello", "from", "broadway"]
a.reverse()
print(a)