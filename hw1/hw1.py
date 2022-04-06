# hw1.py 
# Isabel Ovalles
# CPSC 3400

print("START OF PROGRAM")

# opening word pairs and words file
wordPairs = open("hw1/threeWords.txt") # get file names for console???"
wordLibrary = open("hw1/words.txt") 

for line in wordPairs:
  line = line.rstrip()
  pair = line.split()
  
  start = pair[0]
  end = pair[1]

  #If the lengths are NOT the same, don't find a word ladder
  #Else, find the word ladder
  if len(start) != len(end):
    print("** No ladder exists from " + start + "->" + end) 
  else:
    print("** Looking for ladder from " + start + "->" + end)  


print("END OF PROGRAM")