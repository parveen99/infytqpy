#PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    adult_cost=no_of_adults*37550.0
    children_cost=(37550.0/3)*no_of_children
    total_cost=adult_cost+children_cost
    service_tax=total_cost*(7/100)
    total_cost=total_cost+service_tax
    discount=total_cost*(10/100)
    total_ticket_cost=total_cost-discount
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
