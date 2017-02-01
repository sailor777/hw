
# define type of brackets
br='()'
sq_br='[]'
cr_br='{}'
all_brackets = '()[]{}'
result = True

# give a string from User
str_with_brackets=input('Enter string:')

# delete spaces from string
str_with_brackets=str_with_brackets.replace(' ','')

sleft=''
sright=''

for i in range(len(str_with_brackets)//2):
    print("First(%s)=%s , Second(%s)=%s" % (i, str_with_brackets[i],-(i+1), str_with_brackets[-(i+1)]))
    sleft=str_with_brackets[i]
    sright=str_with_brackets[-(i+1)]

    if all_brackets.find(sleft) == -1 and all_brackets.find(sright) == -1:
        print(all_brackets.find(sleft) == -1)
        print(all_brackets.find(sright) == -1)
        result = False
        print("Result=",result)
        break
    else:
        if sleft + sright == br or sleft + sright == sq_br or sleft + sright == cr_br:
            result = True
            print("Result=",result)
            continue
        else:
            result = False
            print("Result=",result)
            break

print("Result of checking brackets in string %r is: %s" % (str_with_brackets,result))
