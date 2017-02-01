
# define
#start_list = [1, [2, 3], ';', [[6, 7, [5], [[[6, 'a']]]]]]
start_list = []
flat_list = []
str_tmp_list = ''

#str_tmp_list = str(start_list)
# or give a string from User
str_tmp_list = str(input('Enter your list in string:'))

str_tmp_list = str_tmp_list.replace('.',',')
str_tmp_list = str_tmp_list.replace(',','')
str_tmp_list = str_tmp_list.replace('\'','')
str_tmp_list = str_tmp_list.replace('[','')
str_tmp_list = str_tmp_list.replace(']','')
str_tmp_list = str_tmp_list.replace(' ','')

start_list = list(str_tmp_list)

for i in start_list:
    try: flat_list.append(int(i))
    except (ValueError): flat_list.append(i)

print("Flat list is: %s" % flat_list)
