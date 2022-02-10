#                                                               Python Utility models /użyteczne modele
# in this section, we look at a few of Python's many standard utility modules to solve common problems.
#
#                                                               File System -- os, os.path, shutil
# the *os* and *os.path* modules include many functions to interact with the file system.
# the *shutil* module can copy files.
# filenames = os.listdir(dir) -- list of filenames in that directory path (not including . and ..). The filenames are just the names in the directory, not their absolute paths.
# os.path.join(dir, filename) -- given a filename from the above list, use this to put the dir and filename together to make a path
# os.path.abspath(path) -- given a path, return an absolute form, e.g. /home/nick/foo/bar.html
# os.path.dirname(path), os.path.basename(path) -- given dir/foo/bar.html, return the dirname "dir/foo" and basename "bar.html"
# os.path.exists(path) -- true if it exists
# os.mkdir(dir_path) -- makes one dir, os.makedirs(dir_path) makes all the needed dirs in this path
# shutil.copy(source-path, dest-path) -- copy a file (dest path directories should exist)
## Example pulls filenames from a dir, prints their relative and absolute paths
def printdir(dir):
  random_filename = os.listdir(dir)
  for random_filename in filenames:
    print(random_filename)  ## foo.txt
    print(os.path.join(dir, random_filename))## dir/foo.txt (relative to current dir)
    print(os.path.abspath(os.path.join(dir, random_filename))) ## /home/nick/dir/foo.txt
# in the interpreter, do an "import os", and then use these commands look at what's available in the module: dir(os), help(os.listdir), dir(os.path), help(os.path.dirname).

#                                                               Running External Processes -- commands
# status, output) = commands.getstatusoutput(cmd) -- runs the command, waits for it to exit, and returns its status int and output text as a tuple.
## the command is run with its standard output and standard error combined into the one output text. The status will be non-zero if the command failed.
## since the standard-err of the command is captured, if it fails, we need to print some indication of what happened.
# output = commands.getoutput(cmd) -- as above, but without the status int.
# there is a commands.getstatus() but it does something else, so don't use it -- dumbest bit of method naming ever!
# if you want more control over the running of the sub-process, see the "popen2" module
# there is also a simple os.system(cmd) which runs the command and dumps its output onto your output and returns its error code.
## this works if you want to run the command but do not need to capture its output into your python data structures.
# the commands module and the popen2 module are deprecated as of Python 2.6 and removed in 3.x. The subprocess module replaces these modules https://docs.python.org/3/library/subprocess.html#subprocess-replacements

## Given a dir path, run an external 'ls -l' on it --
## shows how to call an external program
import sys
def listdir(dir):
  cmd = 'ls -l ' + dir
  print("Command to run:", cmd)   ## good to debug cmd before actually running it
  (status, output) = commands.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(status)
  print(output) ## Otherwise do something with the command's output

#                                                               Exceptions
# an exception represents a run-time error that halts the normal execution at a particular line and transfers control to error handling code.
# this section just introduces the most basic uses of exceptions.
# for example a run-time error might be that a variable used in the program does not have a value (ValueError .. you've probably seen that one a few times), or a file open operation error because a file does not exist (IOError)
# without any error handling code (as we have done thus far), a run-time exception just halts the program with an error message.
# that's a good default behavior, and you've seen it many times. You can add a "try/except" structure to your code to handle exceptions, like this:
try:
    ## Either of these two lines could throw an IOError, say
    ## if the file does not exist or the read() encounters a low level error.
    f = open(random_filename, 'rU')
    text = f.read()
    f.close()
  except IOError:
    ## Control jumps directly to here if any of the above lines throws IOError.
    sys.stderr.write('problem reading:' + random_filename)
  ## In any case, the code then continues with the line after the try/except
# the try: section includes the code which might throw an exception.
# the except: section holds the code to run if there is an exception.
# if there is no exception, the except: section is skipped

#                                                               HTTP -- urllib.request,and urllib.parse
# the module *urllib.request* provides url fetching -- making a url look like a file you can read from.
# the *urllib.parse* module can take apart and put together urls.
# all of their exceptions are in urllib.error.
# urllib.request for opening and reading URLs
# urllib.error containing the exceptions raised by urllib.request
# urllib.parse for parsing URLs
# urllib.robotparser for parsing robots.txt files
# ufile = urllib.urlopen(url) -- returns a file like object for that url
# text = ufile.read() -- can read from it, like a file (readlines() etc. also work)
# info = ufile.info() -- the meta info for that request. info.gettype() is the mime type, e.g. 'text/html'
# baseurl = ufile.geturl() -- gets the "base" url for the request, which may be different from the original because of redirects
# urllib.urlretrieve(url, filename) -- downloads the url data to the given file path
# urlparse.urljoin(baseurl, url) -- given a url that may or may not be full, and the baseurl of the page it comes from, return a full url. Use geturl() above to provide the base url.
## Given a url, try to retrieve it. If it's text/html,
## print its base url and its text.
def wget(url):
  ufile = urllib.urlopen(url)  ## get file-like object for url
  info = ufile.info()   ## meta-info about the url content
  if info.gettype() == 'text/html':
    print('base url:' + ufile.geturl())
    text = ufile.read()  ## read all its text
    print(text)
# the above code works fine, but does not include error handling if a url does not work for some reason.
# here's a version of the function which adds try/except logic to print an error message if the url operation fails.
## Version that uses try/except to print an error message if the
## urlopen() fails.
def wget2(url):
  try:
    ufile = urllib.urlopen(url)
    if ufile.info().gettype() == 'text/html':
      print(ufile.read())
  except IOError:
    print('problem reading url:', url)










