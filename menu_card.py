#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    item_tuple=list(item_tuple)
    for i in range(0,len(item_tuple),2):
        n=0
        for j in range(0,len(menu)-1):
            if(item_tuple[i]==menu[j]):
                n=1
                break
        if(n==0):
            print(item_tuple[i],"is not available")
            break
        else:
            val=check_quantity_available(j,item_tuple[i+1])
        if(val==True):
            print(item_tuple[i],"is available")
        elif(val==False):
            print(item_tuple[i],"stock is over")
                    
    #Remove pass and write your logic here


    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    ans=False
    if(int(quantity_requested)<=quantity_available[index]):
        ans=True
        quantity_available[index]=quantity_available[index]-quantity_requested
    return ans
        
    #Remove pass and write your logic here to return an appropriate boolean value.


#Provide different values for items ordered and test your program
place_order("Veg Roll",2,"Noodles",2)
place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)
