#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    rabbit_count=0 
    chicken_count=0 
    rabbit_count=abs(legs-(heads*2))
    
    if(rabbit_count % 2==0):
        rabbit_count=rabbit_count//2
        chicken_count=abs(heads-rabbit_count)
    if(chicken_count+rabbit_count==heads):
        print(chicken_count,rabbit_count)
    else:
        print(error_msg)

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(20,10)
