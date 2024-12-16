from collections import Counter
import re
import json

Input = {"vjw": "ap", "vsp": "ap", "bng": "ka", "chn": "tn",
         "cmb": "tn", "mys": "ka", "hyd": "tg", "tpt": "ap"}

Output = {"ap": ["vjw", "vsp", "tpt"], "ka": [
    "blr", "mys"], "tg": ["hyd"], "tn": ["chn", "cmb"]}

Result = {}


def GroupCities(Input):
    for city, state in Input.items():
        if state in Result:
            Result[state].append(city)
        else:
            Result[state] = [city]


GroupCities(Input)
# print(json.dumps(Result, indent=4))

words = ['effort', 'FLEE', 'facade', 'oddball', 'rat', 'tool', 'a22b']
Output = ['effort', 'FLEE', 'oddball', 'tool', 'a22b']

ResultWords = []
isRepeating = False
for word in words:
    # print(word)
    # R=[for i in word if word[i] == word[]]
    # for i in range(1word):
    #     if word[i] == word[i+1]:
            
    for char in range(len(word)-1):
        if word[char] == word[char+1]:
            # print(word[char], word[char+1])
            ResultWords.append(word)
            
            # isRepeating = True
            # break
    # if not isRepeating:
    #     ResultWords.append(word)

# print(ResultWords)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


class A(object):
    def __addition(self, Num1, Num2):
        print(f'Added Result : {Num1 + Num2}')

class B(A):
    def __addition(self, Num1, Num2):
        if Num1 < 0:
            print(f'Multiplied Result {Num1*Num2}')
        else:
            super()._A__addition(Num1, Num2)

# A_Obj = A()
B_Obj = B()
# B_Obj.__B__addition(2,3) 
# B_Obj.__B__addition(-2,3) 

B_Obj._B__addition(2,3)
B_Obj._B__addition(-2,3)
# print(dir(B_Obj))
