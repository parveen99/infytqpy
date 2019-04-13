def find_common_characters(msg1,msg2):
    a=''
    for i in range(0,len(msg1)):
        for j in range(0,len(msg2)):
            if(msg1[i]==msg2[j]):
                if(msg1[i]!=" "):
                    if msg1[i] not in str(a):
                        a=a+msg1[i]
    if(a==''):
        a=-1
                
    return a
     #Remove pass and write your logic here

#Provide different values for msg1,msg2 and test your program
msg1="python"
msg2="Python"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
