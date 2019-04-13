

def encode(message):
    wordsize=0
    encoded_message=""
    for i in range(0,len(message)):
        ch=message[i]
        wordsize=wordsize+1 
        if(i==len(message)-1):
            encoded_message=encoded_message+str(wordsize)+ch
            break
        else:
            if(ch==message[i+1]):
                pass
            else:
                encoded_message=encoded_message+str(wordsize)+ch
                wordsize=0
    return encoded_message
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
