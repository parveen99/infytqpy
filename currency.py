#PF-Tryout

def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    eurocurrency_val=0.01417
    britishcurrency_val=0.0100
    Australian_val=0.02140
    Canadian_val=0.02027
    if(current_currency_name=="Euro" or current_currency_name=="British Pound" or current_currency_name=="Australian Dollar" or current_currency_name=="Canadian Dollar"):
        if(current_currency_name=="Euro"):
            currency_needed=amount_needed_inr*eurocurrency_val
        if(current_currency_name=="British Pound"):
            currency_needed=amount_needed_inr*britishcurrency_val
        if(current_currency_name=="Australian Dollar"):
            currency_needed=amount_needed_inr*Australian_val
        if(current_currency_name=="Canadian Dollar"):
            currency_needed=amount_needed_inr*Canadian_val
    else:
        currency_needed=-1
    
    #write your logic here
    current_currency_amount=currency_needed
    return current_currency_amount


#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(2000,"Euro")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
