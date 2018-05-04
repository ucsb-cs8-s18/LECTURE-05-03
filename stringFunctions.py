# stringFunctions.py

somestring = "hello"

def computeVowelCountDict(somestring):
    " return a dictionary with counts for each of 'a','e','i','o','u', if they appear"

    answer = {}

    for c in somestring:
        c = c.lower()
        if c in "aeiou":
            if c in answer:
               answer[c] += 1
            else:
               answer[c] = 1

    return answer
