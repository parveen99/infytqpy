#PF-Assgn-29
def calculate(distance,no_of_passengers):
    price_per_litre=70
    price_per_ticket=80
    mileage=10
    amount=price_per_ticket*no_of_passengers
    litres_required=distance/mileage
    litres_actual_cost=litres_required*price_per_litre
    amount=amount-litres_actual_cost
    if(amount<0):
        amount=-1
    return amount
        
