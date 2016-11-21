lines = []
attributeFieldName = []
newlines = []

filename = ("optall.arff")
with open("optall.txt") as f: #read the file line by line into a list
	#lines = f.readlines()
		for line in f:
			lines.append(line)

counter = 0
for index in range(0,64): #create attribute for each field in the data
	counter += 1
	attributeFieldName.append("@ATTRIBUTE a"+str(counter)+" NUMERIC") #create attribute

attributeClass = "@ATTRIBUTE class {0,1,2,3,4,5,6,7,8,9}" #"@ATTRIBUTE class {0,1}" add class attribute

for index in lines: #For each line in the lines list, the contents are converted from strings to numbers
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

target = open(filename, 'w') #opens the file to write to it
target.write("\n")
target.write("@RELATION opt0") #adds the relation line to the file
target.write("\n")
for index in attributeFieldName: #adds each attribute to its own line in the file
	target.write(index)
	target.write("\n")

target.write(attributeClass) # adds the class attribute to the file
target.write("\n")

target.write("@DATA")
target.write("\n")

counter = 0
for index in newlines: #adds every different line of numbers to a line in the new file
	#string = index[:-1]
	target.write(index)
	target.write("\n")
	counter+=1
