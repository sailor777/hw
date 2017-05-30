start_list = [1, [2, 3], ';', [[6, 7, [5], [[[6, 'a']]]]]]

def make_flat_list(args):
    flat_list = []
    for item in args:
        if isinstance(item, list):
            if isinstance(item, list):
                flat_list += make_flat_list(item)
            else:
                [flat_list.append(i) for i in item]
        else:
            flat_list.append(item)
    return flat_list

print("Flat list is: %s" % make_flat_list(start_list))
