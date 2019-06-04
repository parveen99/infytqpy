#PF-Assgn-46

def nearest_palindrome(number):
    #start writitng your code here
    f=1
    while(f==1):
        number+=1 
        nnumber=str(number)
        n1=nnumber[::-1]
        if(nnumber==n1):
            f=0
    return number
number=12300
print(nearest_palindrome(number))
