
reqd_gems=['Ivory', 'Quartz']
reqd_quantity=[5, 8]
gems_list=['Moonstone', 'Sapphire', 'Quartz']
price_list=[3498, 1257, 5467]
#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic her
    for i in range(0,len(reqd_gems)):
        if reqd_gems[i] in gems_list:
            flag=1
            j=gems_list.index(reqd_gems[i])
            bill_amount=bill_amount+price_list[j]*reqd_quantity[i] 
        else:
            flag=0
    if(flag==0):
        bill_amount=-1
    else:
        if(bill_amount>30000):
            bill_amount_dis=(bill_amount*0.05)
            bill_amount=bill_amount-bill_amount_dis
    
    return bill_amount


bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
