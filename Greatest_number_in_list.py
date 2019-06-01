#PF-Assgn-36
def create_largest_number(number_list):
    ss=""
    
    #remove pass and write your logic here
    number_list.sort(reverse=True)
    for i in number_list:
        ss=ss+str(i)
    return int(ss)
        

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
