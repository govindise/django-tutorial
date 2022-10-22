'''
temp = [0, 10, 15, 20, 1, 5, 60, 8, 79, 0]

peek_list = []
trough_list = []

for i in range(len(temp)) :
        data_point = temp[i]
        if len(peek_list) == 0 :
                peek_list.append(data_point)
        elif peek_list[-1] <= data_point :
                peek_list.append(data_point)
        else :
                trough_list.append(data_point)

print(peek_list)
print(trough_list)


# Reformatting Dictionary
# Present format:
# *************
source = [{"text1":"ELECTRICAL",
          "dryer1":"60",
          "dryer2":"60",
          "dryer3":"60",
          "dryer4":"60"},
          
          {"text1":"THERMAL",
          "dryer1":"50",
          "dryer2":"50",
          "dryer3":"50",
          "dryer4":"50"},
          
          {"text1":"COMBINED",
          "dryer1":"40",
          "dryer2":"40",
          "dryer3":"40",
          "dryer4":"40"}]


# TO BE format:
# *************
destination = [{"dryer":"1","thermal":"50","electrical":"60","combined":"40"},
               {"dryer":"2","thermal":"50","electrical":"60","combined":"40"},
               {"dryer":"3","thermal":"50","electrical":"60","combined":"40"},
               {"dryer":"4","thermal":"50","electrical":"60","combined":"40"}]

from audioop import reverse
from logging import StringTemplateStyle
from turtle import position
import pandas as pd

def func(string) :
        return string[-1]

sourceDataFrame = pd.DataFrame(source)
destinationDataFrame = pd.DataFrame(destination)

sourceDataFrame = sourceDataFrame.transpose().reset_index()
sourceDataFrame = sourceDataFrame.iloc[1:]
sourceDataFrame.columns=['Dryer', 'Thermal', 'Electrical', 'Combined']
sourceDataFrame['Dryer'] = sourceDataFrame['Dryer'].apply(func)


fibonacci_list = []

def fibonacci(number) :
        if number == 0 :
                fibonacci_list.append(number)
                return 0
        if number == 1 :
                fibonacci_list.append(number)
                return 1
        
        fibonacci_list.append(number)
        
        return fibonacci(number-1) + fibonacci(number-2)

fibonacci(10)
print(fibonacci_list)

input = '5 dup + 8 pop dup + 9 -'
input_list = input.split(' ')
stack = []

for element in input_list :
        try :
                if type(int(element)) == int :
                        stack.append(int(element))
        except :
                if element == 'dup' :
                        stack.append(stack[-1])
                
                elif element == '+' :
                        data1 = stack.pop()
                        data2 = stack.pop()
                        stack.append(data1 + data2)
                
                elif element == '-' :
                        data1 = stack.pop()
                        data2 = stack.pop()
                        
                        if data1 > data2 :
                                stack.append(data1 - data2)
                        else :
                                stack.append(data2 - data1)
                
                elif element == 'pop' :
                        stack.pop()

print(stack)


string = 'Govindaraju'
reverse_string = ''
for i in range(len(string)) :
        reverse_string = reverse_string + string[len(string) - i - 1]

print(reverse_string)



frequency = {}
numbers = [2, 5, 2, 1, 3, 2, 4, 5, 2, 7, 4, 2, 3, 5, 7, 5, 4, 3, 5, 5, 4]
unique_numbers = list(set(numbers))

for number in unique_numbers :
        frequency[number] = 0

for number in numbers :
        frequency[number] = frequency[number] + 1


# Using Bubble Sort Technique
#############################
sorted_frequency = []
for key, value in frequency.items() :
        sorted_frequency.append([key, value])

for i in range(len(sorted_frequency)-1) :
        for j in range(len(sorted_frequency)-i-1) :
                if sorted_frequency[j][1] <= sorted_frequency[j+1][1] :
                        temp = sorted_frequency[j]
                        sorted_frequency[j] = sorted_frequency[j+1]
                        sorted_frequency[j+1] = temp


sorted_frequency = sorted(frequency.items(), key=lambda item: item[1])
sorted_frequency_list = []

for i in sorted_frequency :
        for j in range(i[1]) :
                sorted_frequency_list.append(i[0])

sorted_frequency_list.reverse()
print(sorted_frequency_list)


# Generators
################################################
def generator() :
        yield 1
        yield 2
        yield 3

x = generator()

print(x.__next__())
print(x.__next__())
print(x.__next__())


# Decorators
################################################
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")
        returned_value = func(*args, **kwargs)
        print("after Execution")
        return returned_value
    return inner1
 
# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
 
# getting the value through return of the function
a, b = 1, 2
print("Sum =", sum_two_numbers(a, b))


# Ordered Dictionary
##############################################
from collections import OrderedDict
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)
 
print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
 
for key, value in od.items():
    print(key, value)


# Find Peaks & Troughs In List Of Numbers
##################################################
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import numpy as np

x = electrocardiogram()[2000:4000]
plt.plot(x)
plt.plot(np.zeros_like(x), "--", color="gray")

peaks, _ = find_peaks(x, height=0)
plt.plot(peaks, x[peaks], "x")

troughs, _ = find_peaks(-x, height=0)
plt.plot(troughs, x[troughs], "x")
plt.show()


# Overloading Not Supported In Python, Converteed Into Override
###############################################################
def temp() :
        print("temp(), Without Parameters")
temp()
print(id(temp))

def temp(x) :
        print("temp(x), With Parameters")
temp(1)
print(id(temp))


# Get Max Number & Position Based On Max Position
#################################################
def getMaxNumberAndPosition(inputList, position) :
        if position >= len(inputList) :
                return ('NA','Invalid Position')
        else :
                uniquInputList = set(inputList)
                sorteInputList = sorted(uniquInputList)
                element = sorteInputList[len(sorteInputList)-position]
                elementPosition = inputList.index(element)
                print("Input: ", inputList)
                print("Sorted Input: ", sorted(inputList))
                return (element, elementPosition)

inputList = [2, 3, 6, 6, 5, 1]
position = 4
output = getMaxNumberAndPosition(inputList, position)
print("Output: ", output)


# Select Random Element For List
################################
import random
import secrets

charecters = ['a', 'b', 'c', 'd', 'e']
print(random.choice(charecters))

integers = [1, 2, 3, 4, 5]
print(random.choice(integers))

strings = ['battery', 'correct', 'horse', 'staple']
print(secrets.choice(strings))


# Sort List Of Dict Based On Number Of Elements in Dict
#######################################################
# input = {'a':[10], 'b':[10,20,30], 'd':[10,20,30,40], 'c':[10,20]}
# output- [{'d': [1j0, 20, 30, 40]}, {'b': [10, 20, 30]}, {'c': [10, 20]}, {'a': [10]}]
input = {'a':[10], 'b':[10,20,30], 'd':[10,20,30,40], 'c':[10,20]}
output = []

# Find Length
dictLength = {}
for key, value in input.items() :
        dictLength[key] = len(value)

# Perform Sorting
sortedList = sorted(dictLength.items(), key=lambda item: item[1])

# Generate Output Data
for i in range(len(sortedList)) :
        output.append({sortedList[i][0]:input[sortedList[i][0]]})

# Generate Sorted Output Data
output.reverse()
print(output)


# Sort list based on integer number in the string
#################################################
input = ["as2hhhvnbvhv", "ji7hhhjg", "ki9ggh.hghg", "ju6gffghf"]
sortedInput = sorted(input, key=lambda x:x[2])
print(sortedInput)


# Method Order Resolution
##########################
class a:
    def display():
        print('class a')

class b:
    def display():
        print('class b')

class c(a, b) :
    def display():
        print('class c')

object = c()
c.display()


# Add numbers in list
#####################
from itertools import zip_longest

li=[1,2,3,4]
lis=[4,5,6,7,8]

additionList = [x + y for x, y in zip_longest(li, lis, fillvalue=0)]
print(additionList)


# Printable Representation Of Variables
repr(additionList)


# Map Function
##############
numbers = (1, 2, 3, 4)
result = map(lambda x : x + x, numbers)
print(list(result))


# Reduce Function
#################
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y : x * y, numbers)
print(result)


# Index Slicing
###############
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[-5:-3])
print(a[4::-2])

x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2][1][2])
print([x[1][2][1], x[1][2][2]])


# Simple decorator
##################
def decoratorFunction(func) :
        def inner(*args, **kwargs) :
                result = func(*args, **kwargs)
                return result
        return inner

@decoratorFunction
def add(x, y) :
        return x+y

print(add(10,11))


# DataFrame From Dictionary
###########################
import pandas as pd
data = {'a': [1], 'b': [2], 'c': [3]}
dataFrame = pd.DataFrame.from_dict(data)
print(dataFrame.info())
dataFrame['a'] = dataFrame['a'].astype(str)
print(dataFrame.info())



# Sort Data Based On Property Values
####################################
class student:
        def __init__(self,id,name,age,grade,score):
                self.id = id
                self.name = name
                self.age = age
                self.grade = grade
                self.avgScore = score
		
obj1 = student(1,"John",19,"B",72)
obj2 = student(1,"Elina",20,"B",70)
obj3 = student(1,"Charlie",21,"C",62)
obj4 = student(1,"Teddy",20,"A",82)

studentList = [obj1,obj2,obj3,obj4]
sorted_list = sorted(studentList, key=lambda obj: obj.name)

for object in sorted_list :
        print(object.name)



# Find Difference Between Two Dictionay
#######################################
input1 = {"key1":
                {
                        "sub_key1":{
                                        "list_key1":[{"":"", "list_key2":""}]
                                   },
                        "sub_key2":{"list_key1":"", "list_key2":""},
                        "sub_key3":[
                                        {"list_key1":"", "list_key2":""}, 
                                        {"list_key1":"", "list_key2":""}
                                   ],
                },
          "key2":"", 
          "key3":{"sub_key1":[{"list_key1":"", "list_key2":""}, {"list_key1":"", "list_key2":""}]}
         }
input2 = {"key1":
                {
                        "sub_key1":[{"list_key1":"", "list_key2":""}, {"list_key1":"", "list_key2":""}], 
                        "sub_key2":"",
                        "sub_key3":"",
                }, 
          "key2":""
         }

stringlist1 = []
for key1, value1 in input1.items() :
        if type(value1) == dict :
                for key2, value2 in value1.items() :
                        stringlist1.append(f'root[{key1}][{key2}]')

stringlist2 = []
for key1, value1 in input2.items() :
        if type(value1) == dict :
                for key2, value2 in value1.items() :
                        stringlist2.append(f'root[{key1}][{key2}]')

set1 = set(stringlist1)
set2 = set(stringlist2)
diff = set1.union(set2) - set1.intersection(set2)
print(diff)


# Using deepdiff
################
from deepdiff import DeepDiff, Delta
diff = DeepDiff(input1, input2)
delta = Delta(input1, input2)

print(diff)
print(delta)


# Bubble Sort
elements = [5, 1, 4, 3, 6, 0, 7, 2, 9, 8]
print("Input Elements: ", elements)

for i in range(len(elements)) :
        for j in range(len(elements)-i-1) :
                if elements[j] >= elements[j+1] :
                        temp = elements[j]
                        elements[j] = elements[j+1]
                        elements[j+1] = temp

print('Sorted Elements: ', elements)


# Find Missing Values From List
###############################
names1 = ['sanjay', 'santosh', 'yashoda', 'seetharam']
names2 = ['sanJay', 'sanTosh', 'yasHoda']

names1 = [x.lower() for x in names1]
names2 = [x.lower() for x in names2]

set1 = set(names1)
set2 = set(names2) 
missingNames = set1.symmetric_difference(set2)

print(missingNames)

import time
 
def differenceDecorator(func):
        def inner1(*args, **kwargs):
                begin = time.time()
                differenceList = func(*args, **kwargs)
                end = time.time()
                print("Difference List: ", differenceList)
                print("Total time taken in : ", func.__name__, end - begin)
        return inner1


@differenceDecorator
def getDifference(list1, list2):
        differenceList = []
        if len(list1) >= len(list2) :
                for x in list1 :
                        if x not in list2 :
                                differenceList.append(x)
        else :
                for x in list2 :
                        if x not in list1 :
                                differenceList.append(x)
        
        missingElements = set(list1).symmetric_difference(set(list2))
        
        for x in missingElements :
                differenceList.append(x)
        
        differenceList = list(set(differenceList))
        
        return differenceList
 
getDifference([2, 5, 1, 9, 6, 7], [2, 5, 1, 10, 6, 7])


# Negative Slicing
##################
a = [1,2,3,4,5,6,7,8,9]
print(a[-1:-5])
print(a[-1:-5:-1])


# List Comprehension
####################
List1= ["apple","banana","kiwi"]
vovelList = ['a', 'e', 'i', 'o', 'u']
output = [x for x in List1 if x[0] in vovelList ]
print(output)


# Sort DataFrame Based On Columns
#################################
dataFrame = pd.read_csv('C:\\Users\\govindaraju.seethara\\OneDrive - Covalense Technologies Private Limited\\Desktop\\student.csv', date_parser=['DOB'])

filterDataFrame = dataFrame[dataFrame['Marks'] >= 80]
filterDataFrame['DOB'] = pd.to_datetime(filterDataFrame['DOB'])
print(filterDataFrame)

filterDataFrame = filterDataFrame.sort_values(by=['DOB'])
print(filterDataFrame)


# Pascals Triangle
###################
from math import factorial
 
n = 5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
 
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    
    print()


for i in range(n):
    # adjust space
    print(' '*(n-i), end='')
 
    # compute power of 11
    print(' '.join(map(str, str(11**i))))



# Print first N prime numbers
#############################
n = 100
output = []
for i in range(1,100000000) :
    for j in range(2,i) :
        if i % j == 0 :
            break
    else:
        output.append(i)
        if len(output) == n :
                break
print(output)


# Binary Search
################
def binarySearch(array, element, low, high) :
        mid = (low + high) // 2

        if mid >= len(array) or mid < 0 :
                print("Search Failed")
                return

        if array[mid] == element :
                print("Search Success, Index: ", mid)
        else :
                if element < array[mid] :
                        binarySearch(array, element, low, mid-1)
                else :
                        binarySearch(array, element, mid+1, high)

array = [i for i in range(100)]
element = -3
binarySearch(array, element, 0, len(array))


# Brackets Validator
####################
input = '([{]({(([)})])})'
bracketCount = {'(': 0, '[': 0, '{': 0}

for bracket in input :
        if bracket in ['(', '[', '{'] :
                bracketCount[bracket]+=1
        elif bracket == ')' :
                bracketCount['(']-=1
        elif bracket == ']' :
                bracketCount['[']-=1
        elif bracket == '}' :
                bracketCount['{']-=1

print(bracketCount)


# Perform Charecter Count Operation
###################################
input = "aaaabbbccda"
output = "a4b3c2d1a1"
charecterList = []
counterList = []
counter = 1

for i in range(1, len(input)) :
        if input[i-1] == input[i] :
                counter += 1
        else :
                charecterList.append(input[i-1])
                counterList.append(counter)
                counter = 1

print(charecterList, counterList)


# Assign Nan Values To Rows & Create DataFrame
##############################################
import numpy
data = {'First Name': ['Govind', 'Govind'],
        'Last Name': ['Seetharam', 'Shah'],
        'Middle Name': [numpy.nan, numpy.nan]
}

import pandas as pd
dataframe = pd.DataFrame(data)
print(dataframe)


# Read Json Data To DataFrame & Perform Required Operation
##########################################################
data = {
  "library": {
    "books": [
      {
        "title": "Structure and Interpretation of Computer Programs",
        "authors": [
          "Abelson",
          "Sussman"
        ],
        "isbn": "9780262510875",
        "price": 38.9,
        "copies": 2
      },
      {
        "title": "The C Programming Language",
        "authors": [
          "Kernighan",
          "Richie"
        ],
        "isbn": "9780131103627",
        "price": 33.59,
        "copies": 3
      },
      {
        "title": "The AWK Programming Language",
        "authors": [
          "Aho",
          "Kernighan",
          "Weinberger"
        ],
        "isbn": "9780201079814",
        "copies": 1
      },
      {
        "title": "Compilers: Principles, Techniques, and Tools",
        "authors": [
          "Aho",
          "Lam",
          "Sethi",
          "Ullman"
        ],
        "isbn": "9780201100884",
        "price": 23.38,
        "copies": 1
      }
    ],
    "loans": [
      {
        "customer": "10001",
        "isbn": "9780262510875",
        "return": "2016-12-05"
      },
      {
        "customer": "10003",
        "isbn": "9780201100884",
        "return": "2016-10-22"
      },
      {
        "customer": "10003",
        "isbn": "9780262510875",
        "return": "2016-12-22"
      }
    ],
    "customers": [
      {
        "id": "10001",
        "name": "Joe Doe",
        "address": {
          "street": "2 Long Road",
          "city": "Winchester",
          "postcode": "SO22 5PU"
        }
      },
      {
        "id": "10002",
        "name": "Fred Bloggs",
        "address": {
          "street": "56 Letsby Avenue",
          "city": "Winchester",
          "postcode": "SO22 4WD"
        }
      },
      {
        "id": "10003",
        "name": "Jason Arthur",
        "address": {
          "street": "1 Preddy Gate",
          "city": "Southampton",
          "postcode": "SO14 0MG"
        }
      }
    ]
  }
}


import pandas as pd

booksDataFrame = pd.DataFrame(data['library']['books'])
loansDataFrame = pd.DataFrame(data['library']['loans'])
customersDataFrame = pd.DataFrame(data['library']['customers'])

customerList = list(customersDataFrame['id'].unique())
resultDataFrame = loansDataFrame.merge(booksDataFrame, on=['isbn'])
resultDataFrame = resultDataFrame[['customer', 'title', 'return']]

output =''
for i in range(len(resultDataFrame)) :
        output += str({resultDataFrame.columns[0]: resultDataFrame.iloc[i][resultDataFrame.columns[0]],
                  resultDataFrame.columns[1]: resultDataFrame.iloc[i][resultDataFrame.columns[1]],
                  resultDataFrame.columns[2]: resultDataFrame.iloc[i][resultDataFrame.columns[2]]
        })

print(output)


input = [1, 2, 3, 4, 5, 'c', 'fds']
squares = [x*x for x in input if type(x) in [int, float]]
print(squares)

input = 'asd asd asdasdas d'
wordList = input.split(' ')
uniquWordList = list(set(wordList))
sortedWordList = sorted(uniquWordList)
print(sortedWordList)


input = [x for x in range(1, 100) if x%4 == 0]
iter(input)
print(input)


# Find Missing Numbers In Series Of Numbers
###########################################
# Approach 1, Using Summation & Difference
n = 5
array = [1, 2, 4, 5]

totalSum = 0
for i in range(1, n+1) :
        totalSum = totalSum + i

arraySum = 0
for number in array :
        arraySum = arraySum + number

missingNumber = totalSum - arraySum
print(missingNumber)


# Approach 2, Using Set Operations
setOfNumbers = {x for x in range(1, n+1)}
setOfArray = set(array)
setOfMissingNumbers = setOfNumbers-setOfArray
print(setOfMissingNumbers)


# Sort Strings Based On Integer Numbers In String
#################################################
input_list = ['4er6', '6fq', '2uyt', '12pouyt']
stringDictionary = {}

for string in input_list :
        number = ''
        for charecter in string :
                try :
                        temp = int(charecter)
                        number = number + charecter
                except :
                        stringDictionary[string] = int(number)
                        break

outputList = sorted(stringDictionary.items(), key=lambda item: item[1])
print(list(dict(outputList).keys()))


input = 'Jun 2022'
# output2 = 'FY22M12'
# input2 = 'July 2022'
# output2 = 'FY23M01'

def findFinancialYearFormat(input) :
        input = input.split(' ')

        monthDitctionary = {
                                'Jan' : 7,
                                'Feb' : 8,
                                'Mar' : 9,
                                'Apr' : 10,
                                'May' : 11,
                                'Jun' : 12,
                                'Jul' : 1,
                                'Aug' : 2,
                                'Sep' : 3,
                                'Oct' : 4,
                                'Nov' : 5,
                                'Dec' : 6,
        }

        if monthDitctionary[input[0]] >= 1 :
                input[1] = str(int(input[1])+1)
        
        output = 'FY' + input[1][-2:] + 'M' + str(monthDitctionary[input[0]])
        print(output)

findFinancialYearFormat(input)
'''

