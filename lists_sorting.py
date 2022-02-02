#                                                                           Lists
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

#                                                                           FOR and IN
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

#                                                                            Range
# the range(n) function yields the numbers 0, 1, ... n-1, and range(a, b) returns a, a+1, ... b-1 -- up to but not including the last number
# the combination of the for-loop and the range() function allow you to build a traditional numeric for loop
## print the numbers from 0 through 99
for i in range(100):
    print(i)

#                                                                              While Loop
# python also has the standard while-loop, and the *break* and *continue* statements work as in C++ and Java
# the above for/in loops solves the common case of iterating over every element in a list, but the while loop gives you total control over the index numbers.

#                                                                              List Methods
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

#                                                                               List Build Up
# one common pattern is to start a list a the empty list [], then use append() or extend() to add elements to it:
listX= []  ## Start as the empty list
listX.append('a')  ## Use append() to add elements
listX.append('b')
print(listX)

#                                                                                List Slices
# slices work on lists just as with strings, and can also be used to change sub-parts of the list.
listB = ['a', 'b', 'c', 'd']
print(listB[1:-1])   ## ['b', 'c']
listB[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(listB)        ## ['z', 'c', 'd']

















