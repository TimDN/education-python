# foo/__init__.py
print("__Init__ running")
from . import bar
# foo/bar.py
print("Imported bar")
def hello():
    print("Hello bar")
#foo/baz.py
print("Imported baz")
# packages.py
import foo
#Prints
# __Init__ running
# Imported bar
foo.bar.hello() #Prints hello bar

