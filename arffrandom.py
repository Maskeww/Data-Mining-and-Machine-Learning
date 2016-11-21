from random import shuffle
lines = []
attributeFieldName = []
newlines = []
randomarray = []

filename = ("optallr.arff")
with open("optall.txt") as f:
		for line in f:
			lines.append(line)
counter = 0
for index in range(0,64): #len(lines[0]) create attributes for each field
	counter += 1
	attributeFieldName.append("@ATTRIBUTE a"+str(counter)+" NUMERIC")

attribute65String = "@ATTRIBUTE class {0,1,2,3,4,5,6,7,8,9}"

for index in lines:
	newstr = []
	newstr1 = []
	newstr2= []
	index = index[:-1]
	numbers = index.split()
	string = str(numbers)
	newstr = string.replace("'", "")
	newstr1 = newstr.replace("[", "")
	newstr2 = newstr1.replace("]", "")
	#print("newstr2", newstr2)
	newlines.append(newstr2)
	#print ("THE NUMBERS ARE HERE", numbers)

target = open(filename, 'w')
target.write("\n")
target.write("@RELATION opt")
target.write("\n")
for index in attributeFieldName:
	target.write(index)
	target.write("\n")

target.write(attribute65String)
target.write("\n")

target.write("@DATA")
target.write("\n")

counter = 0

for index in newlines:
	randomarray.append(index)
	shuffle(randomarray)


for index in randomarray:
		target.write(index)
		target.write("\n")
		counter+=1
