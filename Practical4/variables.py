#4.1 Some simple math 
a=15 #The walk to the bus stop is 15 mins
b=1*60+15 #The bus journey takes 1 hr and 15 mins
c=a+b #the total length of time

d=1*60+30 #The drive takes 1 hr and 30 mins
e=5  #the walk from the car park takes 5 mins
f=d+e #the total length of time for the car-based commute

if c < f:
    quicker_method = "bus"
if c > f: 
    quicker_method = "car"
# Output to check which method is quicker
print("The quicker method is:", quicker_method)
# The output is: The quicker method is: bus
# so comparing c to f, f is longer
# so walking to the bus stop and taking the bus directly to their office (c)) is quicker



#4.2 Booleans
X = True
Y = False
W = X and Y #a new variable called W which encodes the Boolean variable ‘both X and Y’
# W is False

# Truth table for W= both X and Y:
# X       Y       W = X and Y
# True    True    True
# True    False   False
# False   True    False
# False   False   False