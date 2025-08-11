class Box:
    original_size = 10

two_box = Box()

print(two_box.original_size)
two_box.original_size = 20

print("this will print the edited size",two_box.original_size)
del two_box.original_size
print("this will fall back to original one",two_box.original_size)
del Box.original_size
print("this will show error", two_box.original_size)#this will show error