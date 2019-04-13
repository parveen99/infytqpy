#goal of this tryout is to create a function from scratch and invoke it for the given problem
def convert_temp(temp):
    sign=temp[-1]
    temp=int(temp[0:-1])
    if(sign=="C" or sign=="c"):
        tempval=(temp*(9/5)+32)
        tempval=str(tempval)+"F"
    elif(sign=="F" or sign=="f"):
        tempval=((temp-32)*(5/9))
        tempval=str(tempval)+"C"
    return tempval

res=convert_temp('44F')
print(res)
