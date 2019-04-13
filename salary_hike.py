#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    if((job_level==3) or(job_level==4 )or( job_level==5)):
        if(job_level==3):
            hike=15
        if(job_level==4):
            hike=7
        if(job_level==5):
            hike=5
    else:
        hike=0
    hikeamt=current_salary*(hike/100)
    new_salary=int(current_salary+hikeamt)       
  
        
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(14500,5)
print(new_salary)
