#PF-Assgn-37

#Global variables
child_id=(10,20,30,40,50)
child_id=list(child_id)
chocolates_received=[12,5,3,4,6]
def calculate_total_chocolates(child_id,chocolates_received):
    return sum(chocolates_received)
    
    #Remove pass and write your logic here to find and return the total number of chocol
    

def reward_child(child_id_rewarded,extra_chocolates):
    f=0
    if(extra_chocolates<1):
        print("Extra chocolates is less than 1")
    
    else:
        for i in range(0,len(child_id)):
            if(child_id[i]==child_id_rewarded):
                chocolates_received[i]=chocolates_received[i]+extra_chocolates
                f=1
        if(f==1):
            print(chocolates_received)
        else:
            print("Child id is invalid")
            
    
    #Remove pass and write your logic here


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates

reward_child(20,2)
