def check_registration_number(num):
    flag=True
    temp=num
    result_sum=0
    while(temp>0):
        rem=temp%10
        result_sum+=rem
        temp=temp//10
        while(result_sum>9):
            result_sum=check_registration_number(result_sum)
            
    if(result_sum!=9):
        flag=False
    print(flag)
        
        
check_registration_number(9014)
