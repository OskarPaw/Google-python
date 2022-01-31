#                                                         Language Introduction
# python is a dynamic, interpreted (bytecode-compiled) language. There are no type declarations of variables, parameters, functions, or methods in source code.
# this makes the code short and flexible, and you lose the compile-time type checking of the source code.
# python tracks the types of all values at runtime and flags code that does not make sense as it runs.
# Python modules can name their functions and variables whatever they want, and the variable names won't conflict — module1.foo is different from module2.foo

#                                                           Import forms
# the standard "sys" module that contains some standard system facilities, like the argv list, and exit() function.
# with the statement "import sys" you can then access the definitions in the sys module and make them available by their fully-qualified name
import sys
# Now can refer to sys.xxx facilities
#sys.exit(0)
# these are collectively known as the "Python Standard Library." Commonly used modules/packages include:
# sys
# re — regular expressions
# os — operating system interface, file system

#                                                           help(), and dir()
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

#                                                           Strings
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

