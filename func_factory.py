def own_print(glob):
    def some_func(loc):
        return ("%s it\'s %s" % (glob,loc))
    return some_func

# test cases
func1 = own_print("foo")
print(func1("bar"))

func2 = own_print("One")
print(func2("not Two"))
print(func2("not Three"))

func3 = own_print("Fafa")
print(func3("Dodo"))
print(func3("Mimimi"))
