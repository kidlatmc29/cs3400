# hw1.py 
# Isabel Ovalles
# CPSC 3400

print("START OF PROGRAM")

# opening word pairs file
wordPairs = open("hw1/pairs.txt") # get file names for console???

for line in wordPairs:
  line = line.rstrip()
  print(line)

  #If the lengths are NOT the same, don't find a word ladder
  #Else, find the word ladder

print("END OF PROGRAM")