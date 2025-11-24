def getAge(bYear, cYear):
    age = cYear - bYear
    
    return age
from datetime import datetime
# Main #####################################
birtyYear = 0
currentYear = datetime.now().year
print(f"Current year: {currentYear}")
birthYear = int(input("Enter your year of birth (AAAA): "))

if birthYear <= currentYear and birthYear >= 1910:
    myAge = getAge(birthYear, currentYear)
    print("Your age is: " + str(myAge))
else:
    print("The year of birth could not be greater than the current year, and it could not be less than 1910")
