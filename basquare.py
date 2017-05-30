# task_1
a = [1, 2, 34, 5, 16, 21]
print([x for x in a if x % 2 == 0])


# task_2
a = [1, 5, 16, 5, 3, 1, 1, 2, 3]
print({elem: a.count(elem) for elem in set(a)})


# task_3
a = [[0, 1, 2], [3, 4], [5, 6, 7, 8], [9]]

def make_flat(args):
    flat_list = []
    for item in args:
        if isinstance(item, list):
            if isinstance(item, list):
                flat_list += make_flat(item)
            else:
                [flat_list.append(i) for i in item]
        else:
            flat_list.append(item)
    return flat_list

print(make_flat(a))

# task_4
class Dlist(list):

    def __truediv__(self, value):
        """ division elements """
        return Dlist[item / value for item in self]

# task_5
with open('db_sites.txt') as f:
    count_lines = 0
    for line in f:
        count_lines += 1

print(count_lines)

# task_6 for bash
from os import system

system('wc -l db_sites.txt')
