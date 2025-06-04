#Arbitrary Arguments ( Args and Kwargs)

#Args = Arrguments 
#Kwargs = keyword Arrguments

def addition(*args):
    return sum(args)

result = addition(1, 8)
print(result)


def addition(**kwargs):
   return sum(kwargs.values())

result= addition(a=1, b=2,c=3)
print(result)

# Order of arguments in function 
def order_test(a,b,c=4,*args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    return "Successfully Executed !"

result =order_test(12,44,66,3,4,5,6,7,8,p=4,q=5)
print(result)
