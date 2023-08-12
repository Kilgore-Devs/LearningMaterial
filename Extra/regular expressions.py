# regex is a sequence of charactes that form a search patterm
# built-in package 're' to work with RegEx
import re
text = "This sentence is wrote using python"
x = re.search("^This.*python$", text)
print(x)

txt = "The car in America"
y = re.search("^The.*America$", txt) # searches and returns strting with The and ending in America.
print(y)

# findall() returns a list containing all the matches.
text2 = "This is a sentence."
z = re.findall("is", text2)  # returns 'is'
print(z)

a = re.findall("paragraph", text2)
print(a)  # returns [] if no matches

b = re.search("\s", text2)  # returns the first white space
print("The first white-space character is located in position:", b.start())

c = re.split("\s", text2)  # returns a list where string has been split at each match
print(c)
d = re.split("\s", text2, 1)  # splits string at the first occurrence.
print(d)
e = re.sub("\s", "*", text2 + text + txt)  # replaces white space with an *. can do multiple.
print(e)

# match object is an object containing info about the search result. If no results, none is returned.
f = re.search("xyz", text + text2 + txt)  # searches text, text2 and txt for xyz, will return 'None'.
print(f)
# .span() returns a tuple containing the start-, and end positions of the match.
g = re.search(r"\bT\w+", text2)  # looks for start and end position starting at T
print(g.span())

# .string returns the string passed into the function
h = re.search(r"\bT\w+", txt)  # looks for string starting in T
print(h.string)

# .group() returns the part of the string where there was a match
i = re.search(r"\bp\w+", text)  # looks for word starting with p
print(i.group())
"""
 Metacharacters are characters with a special meaning:

Character	Description	                               Example	
[]	    A set of characters	                          "[a-m]"	
\	    Signals a special sequence or escape chars	     "\d"	
.	    Any character (except newline character)	  "he..o"	
^	    Starts with	                                 "^hello"	
$	    Ends with	                                "planet$"	
*	    Zero or more occurrences	                  "he.*o"	
+	    One or more occurrences	                      "he.+o"	
?	    Zero or one occurrences	                      "he.?o"	
{}	    Exactly specified # of occurrences	        "he.{2}o"	
|	    Either or	                            "falls|stays"	
()	    Capture and group	

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	                            Description	                                                            Example  
\A	                 Ret match if specified characters are at the beginning of the string	                     "\AThe"	
\b'	                 Ret match where specified characters are at beginning or end of a word	                    r"\bain"
                                                                                                                r"ain\b"	
\B	                 Ret match where specified chars are present, but NOT at beginning/end of a word            r"\Bain"
                                                                                                                r"ain\B"
\d	                 Ret match where string contains digits (numbers from 0-9)	                                    "\d"
\D                   Ret match where string DOES NOT contain digits	                                                "\D"
\s	                 Ret match where string contains a white space character	                                    "\s"
\S	                 Ret match where string DOES NOT contain a white space character                                "\S"
\w	                 Ret match where string contains any word characters                                            "\w"
                        ^^^(characters from a to Z, digits from 0-9, and the underscore _ character)
\W	                 Ret match where string DOES NOT contain any word characters	                                "\W"
\Z	                 Ret match if specified characters are at the end of the string	                           "Spain\Z"

for \b and \B--the "r" in the beginning is making sure that the string is being treated as a "raw string"


A Set is a set of chars inside of square brackets [] and has a special meaning.
Set	            Description
[arn]	        Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	        Returns a match for any lower case character, alphabetically between a and n	
[^arn]	        Returns a match for any character EXCEPT a, r, and n	
[0123]	        Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	        Returns a match for any digit between 0 and 9	
[0-5][0-9]	    Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	            In sets, +, *, ., |, (), $,{} -no special meaning, so [+] means: return a match for any + char in string
"""