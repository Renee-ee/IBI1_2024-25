w = 55
h = 1.6
bmi = w/h**2
print ("Your bmi is" , str(bmi))
if bmi > 30: 
    print ("You are obese.")
elif bmi < 18.5:
    print ("You are underweight.")
else:
    print ("You are normal weight.")