#For children up to the age of 18, the recommended dose of the painkiller paracetamol is 15 mg/kg.

def drug (w,s):
    if w<10 or w>100 or (s!= 120 and s!= 250): #a number of checks
        return "error"
    else: # if all the check is right, calculate the volume of paracetamol required
        vol = w*s
        return vol

w = 50 #get the weight
s = 120 #get the strength of paracetamol:120 for 120mg/5ml or 250 for 250mg/5ml

print(drug (w,s))