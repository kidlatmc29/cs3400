# hw1.py 
# Isabel Ovalles
# CPSC 3400

def main():
  print("START OF PROGRAM")
  # opening word pairs and words file
  wordPairs = open("hw1/threeWords.txt")
  wordLib = set(open("hw1/words.txt").read().split())
  
  for line in wordPairs:
    start,end = line.split()
    print("\n** Looking for ladder from " + start + "->" + end) 
    # fxn call to findWordLadder()
    findWordLadder(start, end, wordLib)

  wordPairs.close()
  print("\nEND OF PROGRAM")

def findWordLadder(start, end, wordLib):
  # edge case 1 - if start and end are the same word
  if(start == end):
    print("** Ladder from " + start + " to " + end + ": " + start + "->" + end)
    return 0
  # edge case 2 - if start and end lengths are not equal
  elif(len(start) != len(end)):
    print("** No ladder exists from " + start + "->" + end) 
    return 0
  
  # initialize search queue
  queue = [[start]]
  candidates = []

  #while queue: 
  # for every character in start
  for index in range(len(start)):
   for letter in "abcdefghijklmnopqrstuvwxyz" :
    # create a candidate word
    newWord = start[:index] + letter + start[index+1:] 
    # add candidate word to candidates lists
    if newWord in wordLib:
      candidates.append(newWord) 
  return 0  

if __name__ == "__main__":
  main()
