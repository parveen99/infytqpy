def find_hcf(x,y):
    if(x<y):
        mini=x
    else:
        mini=y

    for i in range(1,mini+1):
        if((x%i==0 )and (y%i==0)):
            hcf=i


    return hcf









result=find_hcf(20,30)
print("THE HCF IS",result)
