#PF-Assgn-38

#PF-Assgn-38

def check_double(number):
    
    #Remove pass and write your logic here
    double_number=number+number
    numberlist=list(str(number))
    double_numberlist=list(str(double_number))
    a=len(str(number))
    b=len(str(double_number))
    m=False
    for i in numberlist:
        if i in double_numberlist:
            m=True
    if((sorted(str(number)))==(sorted(str(double_number)))):
        p=True
    else:
        p=False
    if((a==b)and(m==True)and(p==True)):
        final=True
    else:
        final=False
    return final
        

#Provide different values for number and test your program
print(check_double(100))

