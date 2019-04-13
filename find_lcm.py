def find_lcm(x,y):
    if(x>y):
        max=x
    else:
        max=y
    while(1):
        if(max%x==0 and max%y==0):
            lcm=max
            break;
        max=max+1

    return lcm







result=find_lcm(30,40)
print("THE LCM IS",result)
