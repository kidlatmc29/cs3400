# hw1.py 
# Isabel Ovalles
# CPSC 3400

print("START OF PROGRAM")

# opening word pairs file
wordPairs = open("hw1/pairs.txt")

lines = wordPairs.readlines()
# for each line in the pairs.txt file
for line in lines:
  print(line)

print("END OF PROGRAM")