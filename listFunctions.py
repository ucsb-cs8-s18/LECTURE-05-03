def onlyEvenIntegers(someList):

   answer = []
   for blah in someList:
       # if blah%2==0 and type(blah)==int:
       if type(blah)==int and blah%2==0:
           answer.append(blah)
   return answer

if __name__=="__main__":
  sampleList = [3,4,5,7,1]
  print(onlyEvenIntegers(sampleList))
