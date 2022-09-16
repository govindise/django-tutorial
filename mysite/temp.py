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