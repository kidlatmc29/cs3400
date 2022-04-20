# hw1.py 
# Isabel Ovalles
# CPSC 3400

from collections import deque 

# PRE: the needed files are named as pairs.txt and words.txt
# POST: N/A 
def main():
  print("START OF PROGRAM")
  wordPairs = open("pairs.txt")
  wordList = set(open("words.txt").read().split())
  
  for line in wordPairs:
    start,end = line.split()
    print("\n** Looking for ladder from " + start + "->" + end) 
    findWordLadder(start, end, wordList)

  wordPairs.close()
  print("\nEND OF PROGRAM")

# PRE: wordList is a set of words from the file word.txt
# POST: prints out the word ladder given the start and end  words, else will
#         print the appropriate error message
def findWordLadder(start, end, wordList):
  noLadderErrorMsg = "** No ladder exists from " + start + "->" + end
  # edge case 1 - if start and end are the same word
  if(start == end):
    print("** Ladder found: " + start + " to " + end + ": " + start + "->" + end)
    return 0
  # edge case 2 - if start and end lengths are not equal
  elif(len(start) != len(end)):
    print(noLadderErrorMsg) 
    return 0
  # edge case 3 - if end is not in wordLib
  elif(end not in wordList) :
    print(noLadderErrorMsg) 
    return 0
  
  queue = deque()
  searched = set()
  startLength = len(start)

  queue.append([start])
  searched.add(start)

  sameLengthWords = findSameLengthWords(wordList, startLength)

  while(queue):
    ladder = queue.popleft()
    currentWord = ladder[-1]
    for i in range(len(start)):
      candidateWords = findCandidateWords(currentWord)
      for newWord in candidateWords:
        if(newWord == end):
          ladder.append(newWord)
          print("** Ladder found: ", end ="")
          print(*ladder, sep = " -> ")
          return 0
        if(newWord not in searched and newWord in sameLengthWords):
          #print("appending ", ladder," ", newWord)
          queue.append(ladder + [newWord])
          searched.add(newWord)
  
  print(noLadderErrorMsg) 
  return 0
  
# PRE: currentWord is a str
# POST: returns a list of strings of all possible words that are one letter
#        different than currentWord
def findCandidateWords(currentWord):
  tempList = []
  for i in range(len(currentWord)):
    for char in "abcdefghijklmnopqrstuvwxyz":
      newWord = currentWord[:i] + char + currentWord[i+1:]
      tempList.append(newWord)
  return tempList

# PRE: wordList is a set of strings
# POST: returns a set of str that are the same length
def findSameLengthWords(wordList, startLength):
  sameLengthWords = set()
  for word in wordList:
    if len(word) == startLength:
      sameLengthWords.add(word)
  return sameLengthWords
  
if __name__ == "__main__":
  main()
