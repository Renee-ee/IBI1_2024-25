#we can observe that the the number of dots for triangle n is (1+2+3+...+n)
#so let the sum s firstly be 0
#then for i in range(1,11), for loop to get the number of dots in triangle in 10 triangles
s=0
for i in range(1,11):
    s+=i
    print ("the number of dots for triangle",i,"is",s) #print the sum s of each i