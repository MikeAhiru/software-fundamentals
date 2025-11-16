# Algoritm description:
''' 
    Basic calc v1
    Get two numbers
    Add, subs, mult, div
    Print results
'''

# 2. Initialize vars and/or constants (Inputs)
print("Enter Number 1: ")
num1 = float(input())
#print(type(num1))

print("Enter Number 2: ")
num2 = float(input())
#print(type(num2))

# 3. Processes
add= num1+num2
subs= num1-num2
mult= num1*num2
div= num1/num2

# 3.Outputs without f-string

print("Addition: ", add, type (add)) 
print("Substraction: ", subs, type (subs)) 
print("Multiplication: ", mult, type (mult))
print("Division: ", div, type (div)) 

#Output with f-string
print("\n")
print(f"Addition: {add}") 
print(f"Substraction: {subs}") 
print(f"Multiplication: {mult}")
print(f"Division: {div}") 