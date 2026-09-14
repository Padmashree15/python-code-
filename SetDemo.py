print("Demonstration of List")

data = {11,21,51,101,21,11}
data1 = {11,90.80,True,"Hello"}

print("First set data is : ",data)

print("Length of data : ",len(data))

print("Data is Heterogeneous : ",data1)

print("Data is unordered : ",data1)

#print("Data at index 2 : ",data1[2]) NA
print("Data with Unique elements : ",data)

print()
print("Set is mutable")
#Insert element is set

data.add(211)
print("Data after insertation of data : ",data)

#Remove element
data.remove(211)
print("Data after removal : ",data)

data.discard(201)
print("Data after discard : ",data)