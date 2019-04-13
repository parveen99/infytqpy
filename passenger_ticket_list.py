#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    num=100
    if(no_of_passengers>=5):
        num1=no_of_passengers-4
        num=num+num1
        for i in range(0,5):
            a=airline+":"+source[0:3]+":"+destination[0:3]+":"+str(num)
            ticket_number_list.append(a)
            num=num+1
    else:
        num=num+1
        for i in range(0,no_of_passengers):
            a=airline+":"+source[0:3]+":"+destination[0:3]+":"+str(num)
            ticket_number_list.append(a)
            num=num+1
        
        
    #Write your logic here

    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
