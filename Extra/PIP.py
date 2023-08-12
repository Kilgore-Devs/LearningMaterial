# PIP is a package manager.
# Packages contain all the files needed for a module aka libraries.
# check if pip is installed-- C:\Users\Your Name\AppData\Local\Programs\Python\Python*\Scripts>pip --version
# download camelcase package C:\Users\Your Name\AppData\Local\Programs\Python\Python*\Scripts>pip install camelcase
# Find other packages https://pypi.org/.
# list installed packages in the same dir - pip list
import camelcase

c = camelcase.CamelCase()
text = "This is camelcase"

print(c.hump(text))
