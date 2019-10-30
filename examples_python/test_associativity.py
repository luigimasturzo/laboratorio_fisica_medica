a = 1.0e8
b = -0.9999999e8
c = 0.4e-7
print('%.55f' % ((a + b) + c))
print('%.55f' % (a + (b + c)))
print(((a + b) + c) == (a + (b + c)))
