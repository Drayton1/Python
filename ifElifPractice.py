age = 12
height = 120

#and
if age == 12 and height <= 120:
    print("Access granted.")
    
#or
if age >= 12 or height >= 130:
    print("Access not granted.")
    
#elif
if age >= 12 or height >= 130:
    print("Too old and too tall.")
    
elif height < 135:
    print("Too tall. Go!")

#and / or
#age = 45

if age <= 12 or height <= 120 and age <= 13:
    print("Okay.")
elif age >=12:
    print("Too old.")
