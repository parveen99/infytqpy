def check_palindrome(word):
    length_=len(word)
    for i in range(0,(length_//2)+1):
        if(word[i]==word[(length_-1)-i]):
            i=i+1 
        else:
            break
    if(i>length_/2):
        status=True
    else:
        status=False
    return status
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
