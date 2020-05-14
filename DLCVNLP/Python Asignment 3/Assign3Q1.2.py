def my_filter(function,*argument):

    if len(argument)==0:
        return None

    finalresult=[]
    for i in range(len(argument)):
            result=function(argument[i])
            finalresult.append(result)
    return finalresult
def filterOddNum(in_num):

    if(in_num % 2) == 0:
        return True
    else:
        return False
filteredresult = list(my_filter(filterOddNum, 1,2,3,4))
print(filteredresult)