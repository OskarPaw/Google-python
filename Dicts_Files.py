#                                                               Dict Hash Table
# python's efficient key/value hash table structure is called a "dict".
# the contents of a dict can be written as a series of key:value pairs within braces { }, e.g. dict = {key1:value1, key2:value2, ... }.
# the "empty dict" is just an empty pair of curly braces {}.
# looking up or setting a value in a dict uses square brackets, e.g. dict['foo'] looks up the value under the key 'foo'.
# strings, numbers, and tuples work as keys, and any type can be a value
# other types may or may not work correctly as keys (strings and tuples work cleanly since they are immutable)
# looking up a value which is not in the dict throws a KeyError -- use "in" to check if the key is in the dict, or use dict.get(key) which returns the value or None if the key is not present
## Can build up a dict by starting with the the empty dict {}
  ## and storing key/value pairs into the dict like this:
  ## dict[key] = value-for-that-key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print(dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
print(dict['a'])    ## Simple lookup, returns 'alpha'
dict['a'] = 6       ## Put new key/value into dict
'a' in dict         ## True
## print dict['z']                  ## Throws KeyError
if 'z' in dict: print(dict['z'])     ## Avoid KeyError
print(dict.get('z'))  ## None (instead of KeyError)

# a for loop on a dictionary iterates over its keys by default.
# the keys will appear in an arbitrary order.
# the methods dict.keys() and dict.values() return lists of the keys or values explicitly.
# there's also an items() which returns a list of (key, value) tuples, which is the most efficient way to examine all the key value data in the dictionary.
# all of these lists can be passed to the sorted() function.
## by default, iterating over a dict iterates over its keys.
## note that the keys are in a random order.
for key in dict: print(key) ## prints a g o

## exactly the same as above
for key in dict.keys() : print(key)

## get the .keys() list:
print(dict.keys())  ## ['a', 'o', 'g']

## likewise, there's a .values() list of values
print(dict.values())  ## ['alpha', 'omega', 'gamma']

## common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
    print(key, dict[key])

## .items() is the dict expressed as (key, value) tuples
print(dict.items())  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items(): print(k, '>', v)
## a > alpha    o > omega     g > gamma
#  dictionary is one of your greatest tools, and you should use it where you can as an easy way to organize data

#                                                               Dict Formatting
# the % operator works conveniently to substitute values from a dict into a string by name:
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
print(s)# 'I want 42 copies of garfield'

#                                                               Del
# the "del" operator does deletions.
# in the simplest case, it can remove the definition of a variable, as if that variable had not been defined.
# del can also be used on list elements or slices to delete that part of the list and to delete entries from a dictionary.
var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]  ## Delete first element
del list[-2:]  ## Delete last two elements
print(list)  ## ['b']

dict = {'a': 1, 'b': 2, 'c': 3}
del dict['b']  ## Delete 'b' entry
print(dict)  ## {'a':1, 'c':3}

#                                                               Files
# the open() function opens and returns a file handle that can be used to read or write a file in the usual way
# the code f = open('name', 'r') opens the file into the variable f, ready for reading operations, and use f.close() when finished.
# instead of 'r', use 'w' for writing, and 'a' for append
# the standard for-loop works for text files, iterating through the lines of the file (this works only for text files, not binary files).
# the for-loop technique is a simple and efficient way to look at all the lines in a text file:
# Echo the contents of a file
f = open('foo.txt', 'rU')
for line in f:  ## iterates over the lines of the file
    print(line,)  ## trailing , so print does not add an end-of-line char
    ## since 'line' already includes the end-of-line.
f.close()
# reading one line at a time has the nice quality that not all the file needs to fit in memory at one time -- handy if you want to look at every line in a 10 gigabyte file without using 10 gigabytes of memory.
# the f.readlines() method reads the whole file into memory and returns its contents as a list of its lines.
# the f.read() method reads the whole file into a single string, which can be a handy way to deal with the text all at once, such as with regular expressions we'll see later.









