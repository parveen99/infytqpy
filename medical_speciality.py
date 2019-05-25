#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    cp=patient_medical_speciality_list.count('P')
    co=patient_medical_speciality_list.count('O')
    ce=patient_medical_speciality_list.count('E')
    if(cp>co and cp>ce):
        speciality="Pediatrics"
    elif(co>cp and co>ce):
        speciality="Orthopedics"
    elif(ce>co and ce>cp):
        speciality="ENT"
    return speciality
        
#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
