#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)
avg=sum(list_of_marks)/len(list_of_marks)
c=0

def find_more_than_average():
    for i in list_of_marks:
        if(i>avg):
            c+=1 
    percentage=c/len(list_of_marks)*100 
    return percentage
    
    #Remove pass and write your logic here

def sort_marks():
    k=sorted(list_of_marks)
    return k
    
        
    #Remove pass and write your logic here

def generate_frequency():
    for i in range(0,26):
        P=[]
        l=0
        for j in range(o,len(list_of_marks)):
            if(list_of_marks[j]==i):
                l+=1 
        P.append(l)
    return(P)
    
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
