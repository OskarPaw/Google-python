#                                                                                       Lists
#  list literals are written within square brackets [ ].
#  lists work similarly to strings -- use the len() function and square brackets [ ] to access data, with the first element at index 0
colors = ['red', 'blue', 'green']
print(colors[0])  ## red
print(colors[2])  ## green
print(len(colors))  ## 3
# assignment with an = on lists does not make a copy.
# instead, assignment makes the two variables point to the one list in memory.
b = colors  ## Does not copy the list
# the "empty list" is just an empty pair of brackets [ ].
# the '+' works to append two lists, so [1, 2] + [3, 4] yields [1, 2, 3, 4] (this is just like + with strings).

#                                                                                      FOR and IN
# the *for* construct -- for var in list -- is an easy way to look at each element in a list
# do not add or remove from the list during iteration.
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)  ## 30
# python code does not have other syntax to remind you of types, your variable names are a key way for you to keep straight what is going on.
# the *in* construct on its own is an easy way to test if an element appears in a list (or other collection) -- value in collection -- tests if the value is in the collection, returning True/False.
list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print('yay')
# you can also use for/in to work on a string.
# the string acts like a list of its chars, so for ch in s: print ch prints all the chars in a string.

#                                                                                      Range
# the range(n) function yields the numbers 0, 1, ... n-1, and range(a, b) returns a, a+1, ... b-1 -- up to but not including the last number
# the combination of the for-loop and the range() function allow you to build a traditional numeric for loop
## print the numbers from 0 through 99
for i in range(100):
    print(i)

#                                                                                      While Loop
# python also has the standard while-loop, and the *break* and *continue* statements work as in C++ and Java
# the above for/in loops solves the common case of iterating over every element in a list, but the while loop gives you total control over the index numbers.

#                                                                                      List Methods
# list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
# list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
# list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
# list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
# list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
# list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
# list.reverse() -- reverses the list in place (does not return it)
# list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
listA = ['larry', 'curly', 'moe']
listA.append('shemp')         ## append elem at end
listA.insert(0, 'xxx')        ## insert elem at index 0
listA.extend(['yyy', 'zzz'])  ## add list of elems at end
print(listA) ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(listA.index('curly') )   ## 2
listA.remove('curly')         ## search and remove that element
listA.pop(1)                  ## removes and returns 'larry'
print(listA)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
listZ = [11, 22, 33]
listZ.append(0)
print(listZ)  ## [11, 22, 33, 0]

#                                                                                   List Build Up
# one common pattern is to start a list a the empty list [], then use append() or extend() to add elements to it:
listX= []  ## Start as the empty list
listX.append('a')  ## Use append() to add elements
listX.append('b')
print(listX)

#                                                                                   List Slices
# slices work on lists just as with strings, and can also be used to change sub-parts of the list.
listB = ['a', 'b', 'c', 'd']
print(listB[1:-1])   ## ['b', 'c']
listB[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(listB)        ## ['z', 'c', 'd']

#                                                                                   Sorting
# easiest way to sort is with the sorted(list) function, which takes a list and returns a new list with those elements in sorted order.
# the original list is not changed.
a = [5, 1, 4, 3]
print(sorted(a))  ## [1, 3, 4, 5]
print(a)  ## [5, 1, 4, 3]
# it's most common to pass a list into the sorted() function, but in fact it can take as input any sort of iterable collection.
# the sorted() function can be customized through optional arguments.
# the sorted() optional argument reverse=True, e.g. sorted(list, reverse=True), makes it sort backwards.
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print(sorted(strs, reverse=True))   ## ['zz', 'aa', 'CC', 'BB']

#                                                                                  Custom Sorting With key=
# custom sorting, sorted() takes an optional "key=" specifying a "key" function that transforms each element before comparison
# the key function takes in 1 value and returns 1 value, and the returned "proxy" value is used for the comparisons within the sort.
# for example with a list of strings, specifying key=len (the built in len() function) sorts the strings by length, from shortest to longest.
# the sort calls len() for each string to get the list of proxy length values, and then sorts with those proxy values.
strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']
# as another example, specifying "str.lower" as the key function is a way to force the sorting to treat uppercase and lowercase the same:
# "key" argument specifying str.lower function to use for sorting
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']
# you can also pass in your own MyFn as the key function, like this:
## say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']
## write a little function that takes a string, and returns its last letter.
## this will be the key function (takes in 1 value, returns 1 value).
def MyFn(s):
    return s[-1]
## Now pass key=MyFn to sorted() to sort by the last letter:
print(sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']
# to use key= custom sorting, remember that you provide a function that takes one value and returns the proxy value to guide the sorting.

#                                                                                  Sort() method
# the sort() method on a list sorts that list into ascending order, e.g. list.sort()
# alist.sort()            ## correct

#                                                                                  Tuples
# a tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate.
# tuples are like lists, except they are immutable and do not change size
# for example, if I wanted to have a list of 3-d coordinates, the natural python representation would be a list of tuples, where each tuple is size 3 holding one (x, y, z) group.
# to create a tuple, just list the values within parenthesis separated by commas.
# the "empty" tuple is just an empty pair of parenthesis
# accessing the elements in a tuple is just like a list -- len(), [ ], for, in, etc. all work the same.
tuple = (1, 2, 'hi')
print(len(tuple))  ## 3
print(tuple[2])  ## hi
# tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
print(tuple)
# to create a size-1 tuple, the lone element must be followed by a comma.
# tuple = ('hi',)   ## size-1 tuple
# he comma is necessary to distinguish the tuple from the ordinary case of putting an expression in parentheses
# assigning a tuple to an identically sized tuple of variable names assigns all the corresponding values.
# if the tuples are not the same size, it throws an error. This feature works for lists too.
(x, y, z) = (42, 13, "hike")
print(z)  ## hike

#                                                                                 List Comprehensions
# a list comprehension is a compact way to write an expression that expands to a whole list
# suppose we have a list nums [1, 2, 3, 4], here is the list comprehension to compute a list of their squares [1, 4, 9, 16]:
nums = [1, 2, 3, 4]
squares = [n * n for n in nums]   ## [1, 4, 9, 16]
print(squares)
# the syntax is [ expr for var in list ] -- the for var in list looks like a regular for-loop, but without the colon (:).
# the expr to its left is evaluated once for each element to give the values for the new list.
# here is an example with strings, where each string is changed to upper case with '!!!' appended:
strs = ['hello', 'and', 'goodbye']
shouting = [s.upper() + '!!!' for s in strs] ## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']
print(shouting)
# we can add an if test to the right of the for-loop to narrow the result. The if test is evaluated for each element, including only the elements where the test is true.
## Select values <= 2
nums = [2, 8, 1, 6]
small = [n for n in nums if n <= 2]  ## [2, 1]
print(small) ## [2, 1]
## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [s.upper() for s in fruits if 'a' in s]
## ['APPLE', 'BANANA']
print(afruits) ## ['APPLE', 'BANANA']                                 
