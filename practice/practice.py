#this is a comment

#I/O practice

inputFile = open("test.txt")
print("File Name: ", inputFile.name)

lines = inputFile.readlines()

for strLine in lines:
  print(strLine)

print("END OF FILE")