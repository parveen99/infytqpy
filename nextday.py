#PF-Tryout

def generate_next_date(date,month,year):
    #Start writing your code here
    if(month==1 or month==3 or month ==5 or month ==7 or month==8 or month==10):
        if(date>=1 and date<=30):
            next_date=date+1
            next_month=month
            next_year=year
        else:
            next_date=1
            month=month+1
            next_year=year
    if((month==4) or (month==6) or (month==9)or (month==11)):
        if(date>=1 and date<=29):
            next_date=date+1
            next_month=month
            next_year=year
        else:
            next_date=1
            next_month=month+1
            next_year=year
    if(month==2):
        if(date>=1 and date<=27):
            next_date=date+1
            next_month=month
            next_year=year
        else:
            next_date=1
            next_month=month+1
            next_year=year
    if((month==2) and (year%4==0)):
        if(date>=1 and date<=28):
            next_date=date+1
            next_month=month
            next_year=year
        else:
            next_date=1
            next_month=month+1
            next_year=year
    if(month==12):
        if(date>=1 and date<=30):
            next_date=date+1
            next_month=month
            next_year=year
        else:
            next_date=1
            month=1
            next_year=year+1
        
        
        

    print(next_date,"-",next_month,"-",next_year)


generate_next_date(22,3,2011)
