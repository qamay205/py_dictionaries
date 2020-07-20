"""
1. Sum Values
Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
The function should return the sum of the values of the dictionary
"""
def sum_values(my_dictionary):
   total_sum = sum(my_dictionary.values())
   return total_sum

# Uncomment these function calls to test your sum_values function:
# print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
# print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


"""
2. EvenKeys
Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, 
as a parameter. This function should return the sum of the values of all even keys.
"""
def sum_even_keys(my_dictionary):
   counter = 0
   for i in my_dictionary:
       if i%2 == 0:
           counter += my_dictionary[i]
   return counter

# Uncomment these function calls to test your  function:
# print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
# print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


"""
3. Add Ten
Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
The function should add 10 to every value in my_dictionary and return my_dictionary
"""
def add_ten(my_dictionary):
   for i, j in my_dictionary.items():
       my_dictionary[i] = j + 10
   return my_dictionary
 
print(add_ten({1:5, 2:2, 3:3}))

# Uncomment these function calls to test your  function:
# print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
# print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}


"""
4. Values That Are Keys
Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
This function should return a list of all values in the dictionary that are also keys.
"""
def values_that_are_keys(my_dictionary):
  new_list = []
  for i in my_dictionary:
     if i in my_dictionary.values():
        new_list.append(i)
  return new_list
 
# Uncomment these function calls to test your  function:
# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
# print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


"""
5. Largest 
Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
The function should return the key associated with the largest value in the dictionary.
"""
def max_key(my_dictionary):
  largest = max(my_dictionary.values())
  for i in my_dictionary:
     if my_dictionary[i] == largest:
        return i

# Uncomment these function calls to test your  function:
# print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
# print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
