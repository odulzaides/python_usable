def func(seq):
        for x in seq:
            try:
                yield float(x)
            except ValueError:
                yield x
             
a = ['Total', '1', '4', '5', '2']
list(func(a))
print list(func(a))
