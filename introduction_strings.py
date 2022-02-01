#                                                                               Language Introduction
# python is a dynamic, interpreted (bytecode-compiled) language. There are no type declarations of variables, parameters, functions, or methods in source code.
# this makes the code short and flexible, and you lose the compile-time type checking of the source code.
# python tracks the types of all values at runtime and flags code that does not make sense as it runs.
# Python modules can name their functions and variables whatever they want, and the variable names won't conflict — module1.foo is different from module2.foo

#                                                                               Import forms
# the standard "sys" module that contains some standard system facilities, like the argv list, and exit() function.
# with the statement "import sys" you can then access the definitions in the sys module and make them available by their fully-qualified name
import sys
# Now can refer to sys.xxx facilities
#sys.exit(0)
# these are collectively known as the "Python Standard Library." Commonly used modules/packages include:
# sys
# re — regular expressions
# os — operating system interface, file system

#                                                                             help(), and dir()
# inside the Python interpreter, the help() function pulls up documentation strings for various modules, functions, and methods.
# these doc strings are similar to Java's javadoc. The dir() function tells you what the attributes of an object are. Below are some ways to call help() and dir() from the interpreter:
# help(len) — help string for the built-in len() function; note that it's "len" not "len()", which is a call to the function, which we don't want
# help(sys) — help string for the sys module (must do an import sys first)
# dir(sys) — dir() is like help() but just gives a quick list of its defined symbols, or "attributes"
# help(sys.exit) — help string for the exit() function in the sys module
# help('xyz'.split) — help string for the split() method for string objects. You can call help() with that object itself or an example of that object, plus its attribute.
# help(list) — help string for list objects
# dir(list) — displays list object attributes, including its methods
# help(list.append) — help string for the append() method for list objects

 #                                                                           Strings
# python strings are "immutable" which means they cannot be changed after they are created (Java strings also use this immutable style)
# since strings can't be changed, we construct *new* strings as we go to represent computed values. So for example the expression ('hello' + 'there') takes in the 2 strings 'hello' and 'there' and builds a new string 'hellothere'.
# characters in a string can be accessed using the standard [ ] syntax, and like Java and C++,
# python uses zero-based indexing, so if s is 'hello' s[1] is 'e'. If the index is out of bounds for the string, Python raises an error.
# the len(string) function returns the length of a string
# syntax and the len() function actually work on any sequence type -- strings, lists, etc
# the '+' operator can concatenate two strings. Notice in the code below that variables are not pre-declared -- just assign to them and go.

s = 'hi'
print(s[1]) ## i
print(len(s))  ## 2
print(s + ' there')  ## hi there
# unlike Java, the '+' does not automatically convert numbers or other types to string form.
# the str() function converts values to a string form so they can be combined with other strings.
pi = 3.14
#text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is ' + str(pi)  ## yes
print(text)
# the print() operator prints out one or more python items followed by a newline (leave a trailing comma at the end of the items to inhibit the newline

#                                                                         String Methods
# a method is like a function, but it runs "on" an object.
# if the variable s is a string, then the code s.lower() runs the lower() method on that string object and returns the result
# most common string methods:
# s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
# s.strip() -- returns a string with whitespace removed from the start and end
# s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
# s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
# s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
# s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
# s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

#                                                                       String Slices
# the slice s[start:end] is the elements beginning at start and extending up to but not including end. Suppose we have s = "Hello"
# s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4
# s[1:] is 'ello' -- omitting either index defaults to the start or end of the string
# s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
# s[1:100] is 'ello' -- an index that is too big is truncated down to the string length
# the standard zero-based index numbers give easy access to chars near the start of the string. As an alternative,
# negative index numbers count back from the end of the string:
# python uses negative numbers to give easy access to the chars at the end of the string:
# s[-1] is 'o' -- last char (1st from the end)
# s[-4] is 'e' -- 4th from the end
# s[:-3] is 'He' -- going up to but not including the last 3 chars.
# s[-3:] is 'llo' -- starting with the 3rd char from the end and extending to the end of the string.

#                                                                      String %
# the % operator takes a printf-type format string on the left (%d int, %s string, %f/%g floating point),
# and the matching values in a tuple on the right (a tuple is made of values separated by commas, typically grouped inside parentheses):
## Add parentheses to make the long line work:
text = (
    "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down."
    % (3, 'huff', 'puff', 'house'))
print(text)
# that's better, but the line is still a little long. Python lets you cut a line up into chunks, which it will then automatically concatenate.
# so, to make this line even shorter, we can do this:
# Split the line into chunks, which are concatenated automatically by Python
text2 = (
        "%d little pigs come out, "
        "or I'll %s, and I'll %s, "
        "and I'll blow your %s down."
        % (3, 'huff', 'puff', 'house'))
print(text2)
#                                                                   If Statement
# python does not use { } to enclose blocks of code for if/loops/function etc.. Instead,
# python uses the colon (:) and indentation/whitespace to group statements.
# the boolean test for an if does not need to be in parenthesis (big difference from C++/Java), and it can have *elif* and *else*
# any value can be used as an if-test. The "zero" values all count as false: None, 0, empty string, empty list, empty dictionary.
# there is also a Boolean type with two values: True and False
speed = input("")
mood = input("")

if speed >= 80:
    print('License and registration please')
    if mood == 'terrible' or speed >= 100:
        print('You have the right to remain silent.')
    elif mood == 'bad' or speed >= 90:
        print("I'm going to have to write you a ticket.")
    else:
        print("Let's try to keep it under 80 ok?")
