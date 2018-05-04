def onlyEvenIntegers(someList):

   answer = []
   for blah in someList:
       #if blah%2==0 and type(blah)==int:  # WRONG ORDER
       if type(blah)==int and blah%2==0:    # CORRECT ORDER
           answer.append(blah)
   return answer

def squareEachInteger(someList):
    "square each integer in the list; leave everything else alone"

    for i in range(len(someList)):
        # do something with someList[i]
        if type(someList[i])==int:
            someList[i] = someList[i] * someList[i]
    # no need to return

def truncateEachString(someList,maxLength):
    "replace every string with a string of at most length maxLength"

   
    for i in range(len(someList)):
        # do something with someList[i]
        if type(someList[i])==str:
            someList[i] = someList[i][0:maxLength]
    # no need to return
    


if __name__=="__main__":
  sampleList = [3,4,5,7,1]
  print(onlyEvenIntegers(sampleList))
