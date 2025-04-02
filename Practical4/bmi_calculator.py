#give the weight into w
#give the height into h
#calculate bmi
#print bmi
#print suggestion
w = 55 #a person’s weight (in kg)
h = 1.6 #a person’s height (in m).
bmi = w/h**2
print ("Your bmi is" , str(bmi))
if bmi > 30: 
    print ("You are obese.")
elif bmi < 18.5:
    print ("You are underweight.")
else:
    print ("You are normal weight.")