#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    a=[]
    # Write your logic here
    def sum_of_digits(x):
        s=0
        while(x>0):
            r=x%10
            s=s+r 
            x=x//10
        return s
    if(num1<num2):
        for i in range(num1,num2+1):
            if((sum_of_digits(num1)%3==0)and (num1<=99) and (num1%5==0)):
                a.append(num1)
    print(a)
    if(a!=[]):
        max_num=max(a)
     
                
    return max_num
    

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,100)
print(max_num)

