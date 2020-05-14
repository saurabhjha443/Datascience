def my_reduce(function,*argument):
    if len(argument)==0:
        return None
    reduced = argument[0]
    for i in range(1,len(argument)):
        reduced = function(reduced,argument[i])
    return reduced

print(my_reduce(lambda x,y:x+y,1,2,3)) 

print(my_reduce(lambda x,y:x+3,1,2,3)) 

print(my_reduce(lambda x,y:x if x>y else y,1,2,3)) 