
def main():
    print("snake_case:",camel_case())
    


def camel_case():
    camel_case = input("camelCase: ").strip()
    snake_case=""
    
    for letter in camel_case:
        if letter.islower():
            snake_case+=letter
        else:
            snake_case+="_"+ letter.lower() 
    
    return snake_case
main()
