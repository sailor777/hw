#!/usr/bin/env python3.6
# define
str_brackets = ''
str_open = '([{'
str_close = ')]}'
str_tmp = ''
result = True
flag = 0

# give a string from User
str_brackets = input('Enter string with brackets:')

# delete spaces from string
str_brackets = str_brackets.replace(' ','')

for i in str_brackets:
    if str_open.find(i) != -1: # if symbol is open brackets then save it in temp string
        str_tmp += str(i)
    elif str_close.find(i) != -1 : # if next symbol is closed brackets
        if  str_tmp != '' and str_close.index(i) == str_open.index(str_tmp[-1]): #compair it with last open
            str_tmp = str_tmp[:-1] # and delete "pair" if balance brackets correct
        else:
            flag = 1
            break

if flag == 0 and str_tmp == '':
    result = True
else:
    result = False

print("Result of checking balance brackets in string %r is: %s" % (str_brackets,result))
