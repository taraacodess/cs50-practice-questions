#make a function to ask for input

def twttr():
    name=input("enter a word:")
    result=""
    vowel="aeiouAEIOU"
#omit vowel letter
    for l in name:
        if l not in vowel:
            result += l
            

       

    print("output:",result)   

twttr()         