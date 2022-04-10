# hw1.py 
# Isabel Ovalles
# CPSC 3400

from collections import deque 

def main():
  print("START OF PROGRAM")
  # opening word pairs and words file
  wordPairs = open("hw1/pairs.txt")
  wordList = set(open("hw1/words.txt").read().split())
  
  for line in wordPairs:
    start,end = line.split()
    print("\n** Looking for ladder from " + start + "->" + end) 
    # fxn call to findWordLadder()
    findWordLadder(start, end, wordList)

  wordPairs.close()
  print("\nEND OF PROGRAM")

def findWordLadder(start, end, wordList):
  # edge case 1 - if start and end are the same word
  if(start == end):
    print("** Ladder found: " + start + " to " + end + ": " + start + "->" + end)
    return 0
  # edge case 2 - if start and end lengths are not equal
  elif(len(start) != len(end)):
    print("** No ladder exists from " + start + "->" + end) 
    return 0
  #edge case 3 - if end is not in wordLib
  elif(end not in wordList) :
    print("** No ladder exists from " + start + "->" + end) 
    return 0
  
  queue = deque()
  searched = set()
  startLength = len(start)

  queue.append([start])
  searched.add(start)

  # create smaller wordList for specific startWord based on word length
  processedWords = set()
  for word in wordList:
    if len(word) == startLength:
      processedWords.add(word)

  while(queue):
    # pop the first entry 
    ladder = queue.popleft() 
    currentWord = ladder[-1]
    for i in range(len(start)):
     
      candidateWords = findCandidateWords(currentWord)
      for newWord in candidateWords:
        if(newWord == end):
          # print out ladder
          ladder.append(newWord)
          print("** Ladder found: ", ladder)
          return 0
        if(newWord not in searched and newWord in processedWords):
          #print("appending ", ladder," ", newWord)
          queue.append(ladder + [newWord])
          searched.add(newWord)
          # append new ladder if next word is not searched and if in wordList
  
  print("** No ladder exists from " + start + "->" + end) 
  return 0
  

def findCandidateWords(currentWord):
  tempList = []
  for i in range(len(currentWord)):
    for char in "abcdefghijklmnopqrstuvwxyz":
      newWord = currentWord[:i] + char + currentWord[i+1:]
      tempList.append(newWord)
  return tempList

if __name__ == "__main__":
  main()
