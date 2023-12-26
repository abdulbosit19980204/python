# Python RegEx
# A RegEx, or Regular Expression, is asequence of characters that froms a serarch pattern

# RegEx can be used to check if a string contains the specified searcha pattern

# RegEx Module
# Python has a built-in package called re, which can be used to work with not RegEx
# Import the re
import re

# RegEx in python
# When you have imported the re module, you can start using regular expression
txt = "The quick brown fox jumps"
x = re.search("^The.*jumps$", txt)
print(x)  # <re.Match object; span=(0, 25), match='The quick brown fox jumps'>

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match
# findall - Returns a list containing all matches
# search - Returns a Match object if there is match anywhere in the string
# split - Returns a list where the string has been split at each match
# sub -Replace one or many matches with a string
x = re.split("^quick", txt)
print(x)

# Meta characters
# Metacharacters are characters with a special meaning

# character   Description                               Example
# [] == A set of characters                             "[a-m]"
# \ == Signals a special sequence (can also be used to  "\d"
#         escape special character)
# . == Any character (expect newline character)         "he..o"
# ^ == Starts with                                      "^hello"
# $ == Ends with                                        "planet$"
# * == Zero or more occurrences                         "he.*o"
# + == One or more occurrences                          "he.+o"
# ? == Zero or one occurrences                          "he?o"
# {} == Exactly the specified number of occurrences     "he.{2}o"
# | == Either or                                        "falls|stays"
# () == Capture and group
# txt1 = """
# Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of
#  a word (the 'r' in the beginning is making sure that the string is being treated as a 'raw string')
# """
# txt2 = "The quick brown fox jumps",
# txt3 = "The quick brown fox"
# a = [txt1, txt2, txt3]
# for i in a:
#     y = re.search("^quick.b", i)
#     print(y)


# Special Squences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning
# \A  == Returns a match if the specified characters are at the beginning of the string   "\AThe"
# ....

# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning
# [arn] == Returns a match where one of the specified characters (a, r or n) is present
# [a-n] == Returns a match for any lowercase character, alphabetically between a and n
# [^arn] == Returns a match for any character EXPECT a, r or n
# [0-5][5-9] == Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z] == Returns a match for any character aphabetically between a and z, lowercase Or uppercase
# [+] == In sets, + * . | () $ {} has no special meaning, so [+] means: return a match for any + character in the string

# The Findall function
# The findall() function returns a list containing all matches
# Print a list of all matches
txt = "The rain in Spain"
x = re.findall('ai', txt)
print(x)  # ['ai', 'ai'] from rain and Spain
# The list contains the matches in the order they are found
# If no matches are found, an empty list is returned

x = re.findall("Portugal", txt)
print(x)  # [] because there is no any "Portugal" on our text

# The search function

# The search function searches the string for a match, and returns a Match object if there is a match
# If there is more than one match, only the first occurence of the match will be returned
# Search for the first white-space character in the string
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
# The first white-space character is located in position: 3
# If no matches are found, the value None is returned

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)  # None

# The split() Function

# The split function returns a list where the string has been split at each match
# Split at each white-space character
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)  # ['The', 'rain', 'in', 'Spain']

# You can control the number of occurrences by specifying the maxsplit parametr
# Split the string only at the first occurrence
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)  # ['The', 'rain in Spain']

# The sub() function replaces the matches with the text of your choice
# Replace every white space character with  the number 9
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)  # The9rain9in9Spain

# You can control the number of replacements by specifying the count parametr
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)  # The9rain9in Spain

# Match Object

# A Match object is an object containing information about the search and the result
# Note: If there is no match , the value None will be returned, instead of the Match Object

# Do a search that will return a Match Object
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object
# <re.Match object; span=(5, 7), match='ai'>

# The Match object has properties and methods used to retrive information about the search, and the result
# .span() returns a tuple containing the start-, and end position of the match
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# Print the position (start - and end- position) of the first match occurrence
# The regular expression looks for any words that starts with an uppercase "S"
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())  # (12, 17)

# Print the string passed into the function
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)  # The rain in Spain

# Print the part of the string where there was a match
# The regular expression looks for any words that starts with an uppercase "s"

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())  # Spain

