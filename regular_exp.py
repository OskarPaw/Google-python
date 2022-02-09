#                                                     Python Regular Expressions
# In Python a regular expression search is typically written as:  match = re.search(pat, str)
# the re.search() method takes a regular expression pattern and a string and searches for that pattern within the string.
# if the search is successful, search() returns a match object or None otherwise.
# therefore, the search is usually immediately followed by an if-statement to test if the search succeeded:
import re
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# if-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')
# the 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without change which is very handy for regular expressions (Java needs this feature badly!).

#                                                      Basic Patterns
# the most basic patterns which match single chars:
# a, X, 9, < -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves because they have special meanings are: . ^ $ * + ? { [ ] \ | ( ) (details below)
# . (a period) -- matches any single character except newline '\n'
# \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any non-word character.
# \b -- boundary between word and non-word
# \s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]. \S (upper case S) matches any non-whitespace character.
# \t, \n, \r -- tab, newline, return
# \d -- decimal digit [0-9] (some older regex utilities do not support \d, but they all support \w and \s)
# ^ = start, $ = end -- match the start or end of the string
# \ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash. If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to make sure it is treated just as a character.

#                                                      Basic Examples
# The basic rules of regular expression search for a pattern within a string are:
# rhe search proceeds through the string from start to end, stopping at the first match found
# all of the pattern must be matched, but not all of the string
# if match = re.search(pat, str) is successful, match is not None and in particular match.group() is the matching text
## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig')
print(match.group()) ## iii
match = re.search(r'igs', 'piiig')
#print(match.group()) ##  None== AttributeError: 'NoneType' object has no attribute 'group' ## there is no such thing in str as igs
# . = any char but \n
match = re.search(r'..g', 'piiig')
print(match.group()) ## iig
# \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g')
print(match.group()) ## 123
match = re.search(r'\w\w\w', '@@abcd!!')
print(match.group()) ## abc

#                                                       Leftmost & Largest
# first the search finds the leftmost match for the pattern, and second it tries to use up as much of the string as possible -- i.e. + and * go as far as possible (the + and * are said to be "greedy").

#                                                       Repetition
# + -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
# * -- 0 or more occurrences of the pattern to its left
# ? -- match 0 or 1 occurrences of the pattern to its left
## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig')
print(match.group()) ## piii
## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii')
print(match.group()) ## ii
## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print(match.group()) ## 1 2   3
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')
print(match.group()) ## 12  3
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
print(match.group()) ## 123
## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar')
#print(match.group()) ##  None== AttributeError: 'NoneType' object has no attribute 'group' ## there is no such string which stars by b
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar')
print(match.group()) ## bar

#                                                       Emails Example
# Suppose you want to find the email address inside the string 'xyz alice-b@google.com purple monkey'
str = "purple alice-b@google.com monkey dishwasher"
match = re.search(r'\w+@\w+', str)
if match:
    print(match.group())  ## b@google
# the search does not get the whole email address in this case because the \w does not match the '-' or '.' in the address.

#                                                       Square Brackets
# square brackets can be used to indicate a set of chars, so [abc] matches 'a' or 'b' or 'c'.
# the codes \w, \s etc. work inside square brackets too with the one exception that dot (.) just means a literal dot.
# for the emails problem, the square brackets are an easy way to add '.' and '-' to the set of chars which can appear around the @ with the pattern r'[\w.-]+@[\w.-]+' to get the whole email address:
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group())  ## 'alice-b@google.com'
# dash indicates a range, so [a-z] matches all lowercase letters. To use a dash without indicating a range, put the dash last, e.g. [abc-].
# an up-hat (^) at the start of a square-bracket set inverts it, so [^ab] means any char except 'a' or 'b'.

#                                                       Group Extraction
# the "group" feature of a regular expression allows you to pick out parts of the matching text.
# suppose for the emails problem that we want to extract the username and host separately
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())   ## 'alice-b@google.com' (the whole match)
    print(match.group(1))  ## 'alice-b' (the username, group 1)
    print(match.group(2))  ## 'google.com' (the host, group 2)

#                                                       findall
# findall() is probably the most powerful function in the re module.
# above we used re.search() to find the first match for a pattern.
# findall() finds *all* the matches and returns them as a list of strings, with each string representing one match.
## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
for email in emails:
# do something with each found email string
    print(email) ## ['alice@google.com', 'bob@abc.com']

# findall With Files
# for files, you may be in the habit of writing a loop to iterate over the lines of the file, and you could then call findall() on each line. Instead, let findall() do the iteration for you
## Open file
# f = open('randomfileidk.txt', 'r')
## Feed the file text into findall(); it returns a list of all the found strings
# strings = re.findall(r'random pattern idk', f.read())

#                                                       findall and Groups
# the parenthesis ( ) group mechanism can be combined with findall().
# ff the pattern includes 2 or more parenthesis groups, then instead of returning a list of strings, findall() returns a list of *tuples*.
# each tuple represents one match of the pattern, and inside the tuple is the group(1), group(2) .. data.
# so if 2 parenthesis groups are added to the email pattern, then findall() returns a list of tuples, each length 2 containing the username and host, e.g. ('alice', 'google.com').
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print(tuple[0])  ## username
    print(tuple[1])  ## host
# once you have the list of tuples, you can loop over it to do some computation for each tuple.
# if the pattern includes no parenthesis, then findall() returns a list of found strings as in earlier examples.
# if the pattern includes a single set of parenthesis, then findall() returns a list of strings corresponding to that single group

#                                                       Options
# the re functions take options to modify the behavior of the pattern match. The option flag is added as an extra argument to the search() or findall() etc., e.g. re.search(pat, str, re.IGNORECASE).
# IGNORECASE -- ignore upper/lowercase differences for matching, so 'a' matches both 'a' and 'A'.
# DOTALL -- allow dot (.) to match newline -- normally it matches anything but newline. This can trip you up -- you think .* matches everything, but by default it does not go past the end of a line.
## DOT ALL note that \s (whitespace) includes newlines, so if you want to match a run of whitespace that may include a newline, you can just use \s*
# MULTILINE -- Within a string made of many lines, allow ^ and $ to match the start and end of each line. Normally ^/$ would just match the start and end of the whole string.

#                                                       Greedy vs. Non-Greedy (optional)
# suppose you are trying to match each tag with the pattern '(<.*>)' -- what does it match first?
# the result is a little surprising, but the greedy aspect of the .* causes it to match the whole '<b>foo</b> and <i>so on</i>' as one big match.
# the problem is that the .* goes as far as is it can, instead of stopping at the first > (aka it is "greedy").
# there is an extension to regular expression where you add a ? at the end, such as .*? or .+?, changing them to be non-greedy.
# now they stop as soon as they can. So the pattern '(<.*?>)' will get just '<b>' as the first match, and '</b>' as the second match, and so on getting each <..> pair in turn.
# the style is typically that you use a .*?, and then immediately its right look for some concrete marker (> in this case) that forces the end of the .*? run.

#                                                       Substitution (optional)
# the re.sub(pat, replacement, str) function searches for all the instances of pattern in the given string, and replaces them.
# the replacement string can include '\1', '\2' which refer to the text from group(1), group(2), and so on from the original matching text.
# here's an example which searches for all the email addresses, and changes them to keep the user (\1) but have yo-yo-dyne.com as the host.
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher






















