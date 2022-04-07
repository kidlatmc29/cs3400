# hw1.py 
# Isabel Ovalles
# CPSC 3400

def main():
  print("START OF PROGRAM")
  # opening word pairs and words file
  wordPairs = open("hw1/threeWords.txt") # get file names for console???
  wordLibrary = open("hw1/words.txt") 
  
  for line in wordPairs:
    pair = line.split()
    start = pair[0]
    end = pair[1]

    if len(start) != len(end):
      print("** No ladder exists from " + start + "->" + end) 
    else:
      print("** Looking for ladder from " + start + "->" + end) 
      # fxn call to findWordLadder()
      findWordLadder(start, end, wordLibrary)

  wordPairs.close()
  print("END OF PROGRAM")

def findWordLadder(start, end, wordLibrary):
  words = set(wordLibrary)
  # edge case 1 - if start and end are the same word
  if(start == end):
    print("** Ladder from " + start + " to " + end + ": " + start + "->" + end)
    return 0
  
  # initialize search queue
  queue = [[start]]
  candidates = []

  while len(queue) > 0: 
    # for every character in start
    for index in range(len(start)):
      for letter in "abcdefghijklmnopqrstuvwxyz" :
        # create a candidate word
        newWord = start[:index] + letter + start[index+1:] 
        # add candidate word to candidates lists 
        if(newWord in words):
          print("adding " + newWord)
          candidates.append(newWord)
  queue.pop() # for debugging 
  
  return 0  

if __name__ == "__main__":
  main()
