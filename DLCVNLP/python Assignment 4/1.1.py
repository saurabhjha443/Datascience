class Area(object):
    def __init__(self):
        pass

    def cal_area(self,a,b,c):
        s=(a+b+c)/2.0
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print(area)


class Parameter(object):
    def __init__(self):
        pass

    def Take_length(self):
        while (True):
            x = [ float (x) for x in input ( "Enter three sides with space: " ).split( " " )] 
            a,b,c=x[0],x[1],x[2]
            if (a+b)>c and (b+c)>a and (a+c)>b:
                break
            print("Incorrect Values :( Try again  ")     
        return a,b,c 


length=Parameter()

a,b,c=length.Take_length()

area=Area()

area.cal_area(a,b,c)