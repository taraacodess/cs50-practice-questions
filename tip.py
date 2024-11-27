#ask the user enter bill amount
x=float(input("enter bill amount"))
y=float(15/100*x) 
z=f"{y:.2f}"

#now print the result
print(f"leave ${z}")