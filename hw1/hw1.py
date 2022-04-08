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
  #edge case 3 - if end is not in wordLib
  elif(end not in wordLib) :
    print("** No ladder exists from " + start + "->" + end) 
    return 0
  
  # initialize search queue
  queue = [[start]]
  searched = set()

  while(queue) :
    currentWord = queue.pop()[-1] # get the last entry in the candidate set
    searched.add(currentWord)

    if(currentWord == end): #if we find the end word we done
      return 0 
    
    # for every character in start
    for index in range(len(start)):
      for letter in "abcdefghijklmnopqrstuvwxyz" :
        # create candidate word
        newWord = start[:index] + letter + start[index+1:] 
     
        if newWord in wordLib and newWord not in searched:
          queue.append(newWord)
          searched.add(newWord)

  return 0  

if __name__ == "__main__":
  main()
