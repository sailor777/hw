
# define
#start_list = [1, [2, 3], ';', [[6, 7, [5], [[[6, 'a']]]]]]
start_list = []
flat_list = []
str_tmp_list = ''
t = ''

#str_tmp_list = str(start_list)
# or give a string from User
str_tmp_list = str(input('Enter your list in string:'))

str_tmp_list = str_tmp_list.replace('.',',')
#str_tmp_list = str_tmp_list.replace(',','')
str_tmp_list = str_tmp_list.replace('\'','')
str_tmp_list = str_tmp_list.replace('[','')
str_tmp_list = str_tmp_list.replace(']','')
#str_tmp_list = str_tmp_list.replace(' ','')
str_tmp_list += ','

start_list = list(str_tmp_list)

for i in start_list:
    if i != ',':
        t += i
    else:
        try: flat_list.append(int(t))
        except (ValueError): flat_list.append(t.lstrip())
        t = ''

print("Flat list is: %s" % flat_list)
