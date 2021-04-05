##import re

##var = 'python is the programming lang'       # match used to search 1st word of string
##var1 = re.match("python" , var)
##
##print(var1)
##print(var1.group())
##print(var1.start())
##print(var1.end())

##var = 'python is the programming lang'            #search used to search any word in string
##var1 = re.search("the" , var)
##
##print(var1)
##print(var1.group())
##print(var1.start())
##print(var1.end())

##var = 'python is the programming lang'            #search used to search any word in string
##var1 = re.search("The" , var, re.I)
##
##print(var1)
##print(var1.group())
##print(var1.start())
##print(var1.end())

##var = "<html><head><body>"
##
##var1 = re.search("<.*>", var)    # .* method used to search anystring
##print(var1.group())              #greedy method
##print(var1.start())
##print(var1.end())

##var = "<html><head><body>"
##
##var1 = re.search("<.*?>", var)    # .*? method used to search 1st word 
##print(var1.group())               #non-greedy method
##print(var1.start())
##print(var1.end())

##var = "India is better than England"
##var1 = re.search(".* is .*",var)
##print(var1.group())

##var = "India is better than England"
##var1 = re.search("(.*) is (.*)",var)
##print(var1.group())
##print(var1.group(1))
##print(var1.group(2))
##
##
##var = "India is better than England"
##var1 = re.search("(.*) is (.*) (.*)",var)
##print(var1.group())
##print(var1.group(1))
##print(var1.group(2))
##print(var1.group(3))

##var = "INDIA !!! is my country @@@ 2021 with 349 in 43 and NEWDELHI with"
####var1 = re.findall("\d{1,3}",var)
##var1 = re.findall("\D{1,3}",var)
##var2 = re.findall("\w",var)   # everythin but not special character
##var3 = re.findall("\w*",var)
##var4 = re.findall("\W+",var)
##
##print(var1)
##print(var2)
##print(var3)
##print(var4)
##
##

##var = "india is wprld is greatt is eng"

####var1 = re.split("is", var)
####print(var1)
##var1 = re.sub("is", "IS", var)
##print(var1)

##pattern = '^d...a$'
##my_string = "delha"
##var1 = re.search(pattern.my_string)
##print(var1.group())

import re


##pattern = '^d...i'
##my_string = "delhi"
##var1 = re.search(pattern,my_string)
##print(var1.group())

pattern = '[abc]'

##my_string = 'zbadc'
my_string = 'abc de ce'
var1 = re.search(pattern, my_string)
print(var1.group())



















