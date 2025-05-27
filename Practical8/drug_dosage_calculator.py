def drug (w,s):
    if w<10 or w>100: #a number of checks
        return "weight error"
    if s!= 120 and s!= 250: #a number of checks
        return "strength of paracetamol error"
    dose_mg = 15 * w  #For children up to the age of 18, the recommended dose of the painkiller paracetamol is 15 mg/kg.
    # For 120 mg/5ml: volume_ml = (dose_mg / 120) * 5
    # For 250 mg/5ml: volume_ml = (dose_mg / 250) * 5
    vol = (dose_mg / s) * 5 
    return vol

w = 26 #get the weight
s = 120 #get the strength of paracetamol:120 for 120mg/5ml or 250 for 250mg/5ml

print(drug (w,s))