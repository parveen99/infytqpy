#PF-Exer-11

def display(num):
    if num%3==0 and num%5==0:
        message="Zoom"
    elif num%3==0:
        message="Zip"
    elif num%5==0:
        message="Zap"
    else:
        message="Invalid"
    
    #write your logic here
    return message

#Provide different values for num and test your program
message=display(9)
print(message)
